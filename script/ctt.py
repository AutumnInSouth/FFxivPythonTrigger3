from random import random
from time import sleep

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import *

recv_packet = OffsetStruct({
    'cut_result': (EnumStruct(c_ubyte, {
        0x0: "Fail",
        0x1: "Normal",
        0x2: "Great",
        0x3: "Perfect"
    }), 12),
    'progress_result': (c_ubyte, 16),
    'round': (c_ubyte, 28),
    'current_profit': (c_ushort, 36),
    'future_profit': (c_ushort, 40),
})


# game_state
# 0x07: "Start Game",
# 0x09: "Difficulty choice",
# 0x0A: "Felling",
# 0x0B: "Start Next Round"

def event_action_pack(game_state: int, is_next: bool, is_start: bool):
    return {
        'event_id': 6,
        'category': 36,
        'param1': 14 | game_state << 16 | (0 if is_next else 1) << 24,
        'param4': 0 if is_start or is_next else 522,
    }


start_msg = event_action_pack(0x07, False, True)
difficulty_msg = event_action_pack(0x09, False, False) | {'param2': 2}
next_round_msg = event_action_pack(0x0B, True, False)
fell_msg = event_action_pack(0x0A, False, False)  # | {'param2': fell_ans}
evt_start_msg = {'event_id': 6, 'category': 36, }  # | {'target_id' : target_id}
evt_finish_msg = {'event_id': 6, 'category': 36, 'param1': 14, }


class Solver:
    def __init__(self):
        self.pool = list(range(101))
        self.history = list()
        self.prev = self.step = self.progress = self.count = 0

    def score(self, score, progress):
        if not score: return
        self.progress = progress
        self.history.append((self.prev, score))
        if score == "Fail":
            self.pool = [i for i in self.pool if abs(i - self.prev) >= 20]
        elif score == "Normal":
            self.pool = [i for i in self.pool if 10 <= abs(i - self.prev) <= 20]
            self.step = min(self.step, 5)
        elif score == "Great":
            self.pool = [i for i in self.pool if 0 < abs(i - self.prev) <= 10]
            self.step = min(self.step, 3)
        elif score == "Perfect":
            self.pool = [self.prev]

    def solve(self):
        self.count += 1
        if self.count >= 9:
            return
        if self.prev is None:
            ans = 80 if random() > 0.5 else 20
        elif len(self.pool) == 1:
            ans = self.pool[0]
        elif not self.pool:
            raise Exception("No ans")
        elif self.progress < 5 and [i for i in self.history if i[1] == "Great"]:
            ans = [i[0] for i in self.history if i[1] == "Great"][-1]
        else:
            p, s = (self.pool, self.pool[0]) if random() > 0.5 else (reversed(self.pool), self.pool[-1])
            ans = [i for i in p if abs(i - s) <= self.step][-1]
        self.prev = ans
        return self.prev


def find_nearest_tree():
    nearest = None
    nearest_dis = 9999
    me = plugins.XivMemory.actor_table.me
    for a in plugins.XivMemory.actor_table:
        if a.e_npc_id == 0x1e99af:
            dis1 = me.absolute_distance_xy(a)
            if dis1 < nearest_dis:
                nearest = a
                nearest_dis = dis1
    return nearest


recv_opcode = "DesynthResult"


def play():
    target = plugins.XivMemory.actor_table.me  # find_nearest_tree()
    if target is None: raise Exception("No tree")
    solver = Solver()
    plugins.XivNetwork.send_messages('zone', ("EventStart", evt_start_msg | {'target_id': target.id}), response="EventPlay")
    _res = plugins.XivNetwork.send_messages('zone', [
        ("EventAction", start_msg),
        ("EventAction", difficulty_msg),
    ], response=recv_opcode)

    while True:
        res = recv_packet.from_buffer(_res.raw_message)
        # print(res)
        solver.score(res.cut_result.value, res.progress_result)
        if res.progress_result:
            _res = plugins.XivNetwork.send_messages(
                'zone',
                ("EventAction", fell_msg | {'param2': solver.solve()}),
                response=recv_opcode
            )
        elif res.future_profit:
            solver = Solver()
            _res = plugins.XivNetwork.send_messages('zone', [
                ("EventAction", next_round_msg),
                ("EventAction", fell_msg | {'param2': solver.solve()}),
            ], response=recv_opcode)
        else:
            sleep(3)
            plugins.XivNetwork.send_messages('zone', ("EventFinish", evt_finish_msg))
            sleep(.1)
            return


def coin_have():
    return sum(i.count for i in plugins.XivMemory.inventory.get_item_in_containers_by_key(29, "currency"))


game_cnt = 0
have_coin = coin_have()
is_continue = True


def on_stop():
    global is_continue
    is_continue = False
    return False


while is_continue and have_coin < 9999999:
    print(f"coin: {have_coin}/9999999 start game {game_cnt}")
    play()
    print(f"finish game {game_cnt}")
    game_cnt += 1
    have_coin = coin_have()
