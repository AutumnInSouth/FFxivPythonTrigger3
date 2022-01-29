from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.logger import Logger
from .get_integer import *
from .keys import *
from ctypes import c_long

_logger = Logger("chat_log/messages")

world_sheet = realm.game_data.get_sheet('World')
item_sheet = realm.game_data.get_sheet('Item')
territory_type_sheet = realm.game_data.get_sheet('TerritoryType')
map_sheet = realm.game_data.get_sheet('Map')
status_sheet = realm.game_data.get_sheet('Status')
quest_sheet = realm.game_data.get_sheet('Quest')
completion_sheet = realm.game_data.get_sheet('Completion')
event_item_sheet = realm.game_data.get_sheet('EventItem')


def extract_special_message(raw: bytearray):
    if raw.pop(0) != START_BYTE:
        raise Exception("Special Message decode, start byte mismatch")
    type_code = raw.pop(0)
    length = raw.pop(0)
    if len(raw) < length:
        raise Exception("Special Message length invalid")
    data = raw[:length]
    if data[-1] == END_BYTE: del data[-1]
    del raw[:length]
    return type_code, data


def pack_special_message(type_code: int, data: bytearray = bytearray()):
    rtn = bytearray([START_BYTE, type_code, len(data) + 1])
    rtn += data
    rtn.append(END_BYTE)
    return rtn


def extract_interactable_message(raw: bytearray):
    type_code, data = extract_special_message(raw)
    if type_code != SeStringChunkType.INTERACTABLE:
        raise Exception("this is not an interactable message")
    return data.pop(0), data


def pack_interactable_message(interact_type: int, data: bytearray = bytearray()):
    return pack_special_message(SeStringChunkType.INTERACTABLE, bytearray([interact_type]) + data)


class MessageBase(object):
    Type = "Unknown"

    def encode(self):
        return bytearray()

    def encode_group(self):
        return self.encode()

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls()

    def text(self):
        return ''

    def __str__(self):
        return "<%s:%s>" % (self.Type, self.text())


class UnknownMessage(MessageBase):
    Type = "UnknownMessage"

    def __init__(self, raw_data: bytearray):
        self.raw_data = raw_data

    def encode(self):
        return self.raw_data

    @classmethod
    def from_buffer(cls, raw: bytearray):
        ans = cls(raw.copy())
        return raw.clear()

    def text(self):
        return self.raw_data.hex()


class TextMessage(MessageBase):
    Type = "Text"

    def __init__(self, text: str):
        self._text = text

    def encode(self):
        return self._text.encode('utf-8')

    def text(self):
        return self._text

    @classmethod
    def from_buffer(cls, raw: bytearray):
        try:
            next_idx = raw.index(START_BYTE)
        except ValueError:
            next_idx = len(raw)
        try:
            split_idx = raw.index(CHAT_LOG_SPLITTER)
        except ValueError:
            split_idx = len(raw)
        end_idx = min(next_idx, split_idx)
        ans = cls(raw[:end_idx].decode('utf-8', errors='ignore'))
        del raw[:end_idx]
        return ans


class SpecialMessage(MessageBase):
    Type = "UnknownSpecial"

    def __init__(self, type_code: int, data: bytearray):
        self.type_code = type_code
        self.data = data

    def encode(self):
        return pack_special_message(self.type_code, self.data)

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls(*extract_special_message(raw))


class EmphasisItalic(MessageBase):
    Type = "EmphasisItalic"

    def __init__(self, enabled: bool):
        self.enabled = enabled

    def text(self):
        return "enabled" if self.enabled else "disabled"

    def encode(self):
        pack_special_message(SeStringChunkType.EMPHASIS_ITALIC, make_integer(int(self.enabled)))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        code, data = extract_special_message(raw)
        return cls(bool(get_integer(data)))


class SeHyphen(MessageBase):
    # Just a '–'
    Type = "SeHyphen"

    def text(self):
        return ''

    def encode(self):
        pack_special_message(SeStringChunkType.SE_HYPHEN)

    @classmethod
    def from_buffer(cls, raw: bytearray):
        extract_special_message(raw)
        return cls()


class Interactable(MessageBase):
    Type = "Interactable/Unknown"

    def __init__(self, interact_type: int, data: bytearray):
        self.interact_type = interact_type
        self.data = data

    def encode(self):
        return pack_interactable_message(self.interact_type, self.data)

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls(*extract_interactable_message(raw))

    def text(self):
        return '[%s - %s]' % (self.interact_type, self.data.hex())


class LinkTerminator(Interactable):
    Type = "Interactable/LinkTerminator"

    def __init__(self, interact_type: int = EmbeddedInfoType.LINK_TERMINATOR, data: bytearray = bytearray(b'\x01\x01\x01\xff\x01')):
        super(LinkTerminator, self).__init__(interact_type, data)

    def text(self):
        return ''


class Player(MessageBase):
    Type = "Interactable/Player"

    def __init__(self, server_id: int, player_name: str):
        self.server_id = server_id
        self.player_name = player_name

    def encode(self):
        encoded_name = self.player_name.encode('utf-8')
        return pack_interactable_message(EmbeddedInfoType.PLAYER_NAME, bytearray([
            0x01,
            *make_integer(self.server_id),
            0x01, 0xff,
            *make_integer(len(encoded_name)),
            *encoded_name
        ]))

    def encode_group(self):
        return self.encode() + TextMessage(self.player_name).encode() + LinkTerminator().encode()

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_interactable_message(raw)
        data.pop(0)  # unk1
        server_id = get_integer(data)
        del data[:2]  # unk2,3
        name_len = get_integer(data)
        return cls(server_id, data[:name_len].decode('utf-8', errors='ignore'))

    def text(self):
        if self.server_id:
            return "%s@%s" % (self.player_name, world_sheet[self.server_id]['Name'])
        else:
            return self.player_name


HQ_SYMBOL = "\ue03c"
COLLECT_SYMBOL = "\ue03d"


class Item(MessageBase):
    Type = "Interactable/Item"

    def __init__(self, item_id: int, is_hq: bool = False, is_collect: bool = False, display_name: str = None):
        self.item_id = item_id
        self.is_hq = is_hq
        self.is_collect = is_collect
        self._display_name = display_name

    @property
    def display_name(self):
        if self._display_name is None:
            if self.item_id < 2000000:
                try:
                    self._display_name = item_sheet[self.item_id]["Name"]
                except KeyError:
                    self._display_name = f"Unknown Item: {self.item_id}"
            else:
                try:
                    self._display_name = event_item_sheet[self.item_id]["Singular"]
                except KeyError:
                    self._display_name = f"Unknown Event Item: {self.item_id}"
            if self.is_hq:
                self._display_name += HQ_SYMBOL
            if self.is_collect:
                self._display_name += COLLECT_SYMBOL
        return self._display_name

    def encode(self):
        encoded_name = self.display_name.encode('utf-8')
        item_id = self.item_id
        if self.is_hq: item_id += 1000000
        if self.is_collect: item_id += 500000
        return pack_interactable_message(EmbeddedInfoType.ITEM_LINK, bytearray([
            *make_integer(item_id),
            0x02, 0x01, 0xff,
            *make_integer(len(encoded_name)),
            *encoded_name
        ]))

    def encode_group(self):
        return self.encode() + LINK_SYMBOL + TextMessage(self.display_name).encode() + LinkTerminator().encode()

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_interactable_message(raw)
        item_id = get_integer(data)
        if item_id < 2000000:
            is_hq = item_id > 1000000
            if is_hq: item_id -= 1000000
            is_collect = item_id > 500000
            if is_collect: item_id -= 500000
        else:
            is_hq = False
            is_collect = False
        if len(data) > 3:
            del data[:3]
            name_len = get_integer(data)
            display_name = data[:name_len].decode('utf-8', errors='ignore').rstrip(HQ_SYMBOL)
        else:
            display_name = None
        return cls(item_id, is_hq, is_collect, display_name)

    def text(self):
        msg = "[%s]%s" % (self.item_id, self.display_name)
        if self.is_hq: msg += "(hq)"
        return msg


def raw_to_in_game_coord(pos):
    return pos / 1000


def in_game_to_raw_coord(pos):
    return pos * 1000


c1 = 41 / 2048


def in_game_to_map_coord(pos, scale, offset=0):
    return (pos + offset) * c1 + 2050 / scale + 1


def map_to_in_game_coord(pos, scale, offset=0):
    return (pos - 1 - 2050 / scale) / c1 - offset


class MapPositionLink(MessageBase):
    Type = "Interactable/MapPositionLink"

    def __init__(self, territory_type_id, map_id, raw_x, raw_y, x, y, map_x, map_y):
        self.territory_type_id = territory_type_id
        self.map_id = map_id
        self.raw_x = raw_x
        self.raw_y = raw_y
        self.x = x
        self.y = y
        self.map_x = map_x
        self.map_y = map_y

    @property
    def territory_type(self):
        return territory_type_sheet[self.territory_type_id]

    @property
    def map(self):
        return map_sheet[self.map_id]

    def encode(self):
        return pack_interactable_message(EmbeddedInfoType.MAP_POSITION_LINK, bytearray([
            *make_packed_integer(self.territory_type_id, self.map_id),
            *make_integer(self.raw_x),
            *make_integer(self.raw_y),
            0xff, 0x01
        ]))

    def encode_group(self):
        return self.encode() + LINK_SYMBOL + TextMessage(self.text()).encode() + LinkTerminator().encode()

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_interactable_message(raw)
        territory_type_id, map_id = get_packed_integer(data)
        raw_x = c_long(get_integer(data)).value
        raw_y = c_long(get_integer(data)).value
        map = map_sheet[map_id]
        x = raw_to_in_game_coord(raw_x)
        y = raw_to_in_game_coord(raw_y)
        map_x = in_game_to_map_coord(x, map["SizeFactor"], map["Offset{X}"])
        map_y = in_game_to_map_coord(y, map["SizeFactor"], map["Offset{Y}"])
        return cls(territory_type_id, map_id, raw_x, raw_y, x, y, map_x, map_y)

    def text(self):
        return f"{self.map['PlaceName']} ( {self.map_x:.1f}  , {self.map_y:.1f} )"


class Status(MessageBase):
    Type = "Interactable/Status"

    def __init__(self, status_id):
        self.status_id = status_id

    def encode(self):
        return pack_interactable_message(EmbeddedInfoType.STATUS, bytearray([
            *make_integer(self.status_id),
            0x01, 0x01, 0xFF, 0x02, 0x20
        ]))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_interactable_message(raw)
        return cls(get_integer(data))

    def text(self):
        return status_sheet[self.status_id]["Name"]

    def encode_group(self):
        return self.encode() + LINK_SYMBOL + TextMessage(self.text()).encode() + LinkTerminator().encode()


class QuestLink(MessageBase):
    Type = "Interactable/Quest"

    def __init__(self, quest_id):
        self.quest_id = quest_id

    def encode(self):
        return pack_interactable_message(EmbeddedInfoType.QUEST_LINK, bytearray([
            *make_integer(self.quest_id - 65536),
            0x1, 0x1,
        ]))

    def encode_group(self):
        return self.encode() + LINK_SYMBOL + TextMessage(self.text()).encode() + LinkTerminator().encode()

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_interactable_message(raw)
        return cls(get_integer(data) + 65536)

    def text(self):
        return quest_sheet[self.quest_id]["Name"]


class AutoTranslateKey(MessageBase):
    Type = "AutoTranslateKey"

    def __init__(self, group, key):
        self.group = group
        self.key = key

    def get_text(self):
        try:
            return completion_sheet[self.key]["Text"]
        except KeyError:
            pass
        s = None
        for r in completion_sheet:
            if r["Group"] == self.group:
                s = r["LookupTable"].split("[", 1)[0]
                break
        if s is None:
            return f"unk_{self.group}/{self.key}"
            # raise KeyError("[%s] is not a valid group key" % self.group)
        try:
            return realm.game_data.get_sheet(s)[self.key]["Name"]
        except KeyError:
            return f"Unknown Data [{s}/{self.key}]"

    def encode(self):
        return pack_special_message(SeStringChunkType.AUTO_TRANSLATE_KEY, bytearray([
            self.group,
            make_integer(self.key)
        ]))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        _, data = extract_special_message(raw)
        return cls(data.pop(0), get_integer(data))

    def text(self):
        return self.get_text()


class UIForeground(MessageBase):
    Type = "UIForeground"

    def __init__(self, color):
        self.color = color

    def encode(self):
        return pack_special_message(SeStringChunkType.UI_FOREGROUND, make_integer(self.color))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls(get_integer(extract_special_message(raw)[1]))

    def text(self):
        return self.color


class UIGlow(MessageBase):
    Type = "UIGlow"

    def __init__(self, color):
        self.color = color

    def encode(self):
        return pack_special_message(SeStringChunkType.UI_GLOW, make_integer(self.color))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls(get_integer(extract_special_message(raw)[1]))

    def text(self):
        return self.color


class Icon(MessageBase):
    Type = "Icon"

    def __init__(self, icon_id):
        self.icon_id = icon_id

    def encode(self):
        return pack_special_message(SeStringChunkType.ICON, make_integer(self.icon_id))

    @classmethod
    def from_buffer(cls, raw: bytearray):
        return cls(get_integer(extract_special_message(raw)[1]))

    def text(self):
        return self.icon_id


LINK_SYMBOL = UIForeground(500).encode() + UIGlow(501).encode() + '\ue0bb'.encode('utf-8') + UIForeground(0).encode() + UIGlow(0).encode()
