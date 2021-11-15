from ctypes import *
from time import sleep
from typing import TYPE_CHECKING

from FFxivPythonTrigger import PluginBase, wait_until, plugins, AddressManager, PluginNotFoundException
from FFxivPythonTrigger.hook import PluginHook
from FFxivPythonTrigger.memory import read_ushort
from FFxivPythonTrigger.decorator import event

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.triple_triad_game_desc import ServerTripleTriadGameDescEvent

command = "@linkross"
card_exist_func = CFUNCTYPE(c_ubyte, c_uint64, c_ushort)
card_check_func_sig = "40 53 48 83 EC ? 48 8B D9 66 85 D2 74 ?"
card_check_module_sig = "48 8D 0D * * * * 89 7C 24 ? 8D 57 ?"
talk_hook_sig = "E8 * * * * 4C 8B 75 ? 4D 3B FE"

FOCUS = 1
CURRENT = 2

from .network import *
from .game import *
from .solvers import SolverBase, SolverA


class Linkross(PluginBase):
    name = "Linkross"

    def __init__(self):
        super().__init__()

        am = AddressManager(self.name, self.logger)
        self.card_check_module = am.scan_point('card_check_module', card_check_module_sig)
        self._card_exist_func = card_exist_func(am.scan_address('card_check_func', card_check_func_sig))
        self.talk_hook(self, am.scan_point('talk_hook', talk_hook_sig))
        self.storage.save()

        self.solvers = [SolverA.Solver]
        self.solver_used = None
        self.card_event = None
        self.available_cards = []
        self.auto_next = 0
        self.refresh_available_cards()
        self.register_command()

    def card_exist(self, card_id: int):
        return bool(self._card_exist_func(self.card_check_module, card_id))

    def refresh_available_cards(self):
        self.available_cards = [Card(row.key) for row in card_sheet if row.key and self.card_exist(row.key)]
        self.logger(f"load {len(self.available_cards)} available cards:\n{','.join(map(str, self.available_cards))}")

    @event("network/zone/server/triple_triad_game_desc")
    def init_rules(self, evt: 'ServerTripleTriadGameDescEvent'):
        data = evt.struct_message
        if data.category != 0x23: return
        rules = set(data.rules)
        self.solver_used = None
        for solver_class in self.solvers:
            solver = solver_class(self.card_event, self.available_cards, rules)
            if solver.suitable():
                self.solver_used = solver
                return
        self.solver_used = "No Solver"

    @PluginHook.decorator(c_uint64, [c_uint64, c_uint64], True)
    def talk_hook(self, hook, a1, a2):
        r = hook.original(a1, a2)
        if self.card_event and read_ushort(a2 + 10) == 0x9:
            talk_finish(read_ushort(a2 + 8))
        return r

    def _play_game(self, mode):
        target = plugins.XivMemory.targets.focus if mode == FOCUS else plugins.XivMemory.targets.current if mode == CURRENT else None
        if target is None: raise Exception(f"Unknown mode: {mode}")
        self.card_event = CardEvent.from_actor(target)
        event_id = self.card_event.event_id
        game_start(event_id, target.b_npc_id)
        solver = wait_until(lambda: self.solver_used, timeout=5)
        if not isinstance(solver, SolverBase): raise Exception(f"No Solver Found")
        confirm_rule_1(event_id)
        confirm_rule_2(event_id)
        deck = solver.get_deck()
        self.logger(",".join([f"{card.card_id}:{card.name}[{card.card_type}]({card.stars})" for card in [Card.get_card(cid) for cid in deck]]))
        import ctypes
        deck_list = list(deck)
        data = choose_cards(event_id, (ctypes.c_ulong * len(deck_list))(*deck_list)).struct_message
        game = Game(BLUE if data.blue_first else RED, data.blue_card, data.red_card, data.rules[:])
        r_data = place_card(event_id, game.round, *(solver.solve(game, data.force_hand_id) if game.current_player == BLUE else [])).struct_message
        game.place_card(r_data.block_id, r_data.hand_id, r_data.card_id)
        win = game.win()
        while win is None:
            #self.logger(game)
            if game.current_player == BLUE:
                choose = solver.solve(game, r_data.force_hand_id)
                #self.logger(choose)
                r_data = place_card(event_id, game.round, *choose).struct_message
            else:
                r_data = place_card(event_id, game.round).struct_message
            game.place_card(r_data.block_id, r_data.hand_id, r_data.card_id)
            win = game.win()
        #self.logger(game)
        self.logger("Blue win!" if win == BLUE else "Red win!" if win == RED else "Draw!")
        solver.end(game)
        end_game(event_id)
        game_finish(event_id)
        self.solver_used = None
        self.card_event = None

    def play_game(self, mode):
        self._play_game(mode)
        while self.auto_next:
            sleep(1)
            self._play_game(mode)

    @event("plugin_load:Command")
    def register_command(self, _):
        try:
            plugins.Command.register(self, command, self.process_command)
        except PluginNotFoundException:
            self.logger.warning("Command is not found")

    def process_command(self, args):
        if args[0] == "f":
            self.create_mission(self.play_game, FOCUS)
        elif args[0] == "c":
            self.create_mission(self.play_game, CURRENT)
        elif args[0] == "auto_next":
            self.auto_next = int(not self.auto_next)
            return f"auto_next:{self.auto_next}"
