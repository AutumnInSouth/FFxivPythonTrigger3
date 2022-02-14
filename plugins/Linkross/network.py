from ctypes import *
from typing import TYPE_CHECKING

from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.memory.struct_factory import OffsetStruct

if TYPE_CHECKING:
    from XivNetwork.message_processors.zone_server.triple_triad_game_data import ServerTripleTriadGameDataEvent
    from XivNetwork.message_processors.zone_server.triple_triad_place_card_recv import ServerTripleTriadPlaceCardRecvEvent

recv_duel_action_finish_opcode = 896  # cn5.57

send_client_trigger = OffsetStruct({
    'unk0': (c_uint, 0),
    'event_id': (c_ushort, 0x4),
    'category': (c_ushort, 0x6),
    'target_bnpc_id': (c_uint, 0x18),
    'unk1': (c_uint, 0x1c),
})
send_event_action = OffsetStruct({
    'event_id': c_ushort,
    'category': c_ushort,
    'param0': c_ubyte,
    'param1': c_ubyte,
    'param2': c_ubyte,
    'param3': c_ubyte,
    'param4': c_ubyte,
    'param5': c_ubyte,
    'param6': c_ubyte,
    'param7': c_ubyte,
    'param8': c_ubyte,
    'param9': c_ubyte,
    'param10': c_ubyte,
    'param11': c_ubyte,
}, 16)
send_event_finish = OffsetStruct({
    'event_id': c_ushort,
    'category': c_ushort,
    'unk2': c_uint,
    'unk3': c_uint,
    'unk4': c_uint,
}, 16)


def game_start(event_id, b_npc_id):
    msg = send_client_trigger(category=0x23, event_id=event_id, target_bnpc_id=b_npc_id, unk0=0x32f, unk1=0x1)
    plugins.XivNetwork.send_messages('zone', ('ClientTrigger', msg), recv_duel_action_finish_opcode)


def end_game(event_id):
    finish_massage = send_event_action(category=0x23, event_id=event_id, param3=1, param4=6)
    finish_massage.param8 = 189
    plugins.XivNetwork.send_messages('zone', ('EventAction', finish_massage))


def talk_finish(event_id):
    msg = send_event_finish(category=0x9, event_id=event_id)
    plugins.XivNetwork.send_messages('zone', ('EventFinish', msg))


def game_finish(event_id):
    msg = send_event_finish(category=0x23, event_id=event_id)
    plugins.XivNetwork.send_messages('zone', ('EventFinish', msg), "EventFinish")


def place_card(event_id, round_id, hand_id=5, block_id=9) -> 'ServerTripleTriadPlaceCardRecvEvent':
    return plugins.XivNetwork.send_messages('zone', ('TripleTriadPlaceCardSend', {
        'event_id': event_id,
        'category': 0x23,
        'unk0': 0x4000000,
        'unk1': 0x5,
        'round': round_id,
        'hand_id': hand_id,
        'block_id': block_id,
    }), 'TripleTriadPlaceCardRecv')


def choose_cards(event_id, cards) -> 'ServerTripleTriadGameDataEvent':
    return plugins.XivNetwork.send_messages('zone', ('TripleTriadSelectDeck', {
        'event_id': event_id,
        'category': 0x23,
        'unk0': 0x6000000,
        'unk1': 0x4,
        'cards': cards
    }), 'TripleTriadGameData')


def confirm_rule_1(event_id):
    continue_msg = send_event_action(category=0x23, event_id=event_id, param3=2, param4=2)
    continue_msg.param8 = 1
    plugins.XivNetwork.send_messages('zone', ('EventAction', continue_msg), recv_duel_action_finish_opcode)


def confirm_rule_2(event_id):
    continue_msg = send_event_action(category=0x23, event_id=event_id, param3=1, param4=3)
    continue_msg.param8 = 51
    continue_msg.param9 = 2
    plugins.XivNetwork.send_messages('zone', ('EventAction', continue_msg), recv_duel_action_finish_opcode)
