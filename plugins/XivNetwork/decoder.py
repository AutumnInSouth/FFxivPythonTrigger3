from queue import Queue, Empty as QueueEmpty
from struct import pack
from threading import Lock
from traceback import format_exc
from typing import Iterable, Tuple, List, Optional
from zlib import decompress, MAX_WBITS, compress

from FFxivPythonTrigger.logger import Logger
from .base_struct import BundleHeader, MessageHeader

SAFE_LIMIT = 100
MAGIC_NUMBER = 0x41a05252
MAGIC_NUMBER_BYTES = pack('I', MAGIC_NUMBER)
_logger = Logger("XivNetwork/Decoder")
unpacked_messages = Tuple[BundleHeader, List[bytearray]]


class PacketProcessor(object):
    def __init__(self):
        self.buffer = bytearray()
        self.lock = Lock()
        self.out_queue = Queue()

    def process(self, packet: bytearray):
        self.buffer.extend(packet)
        msg_cnt = 0
        while self.buffer:
            msg_cnt += 1
            if msg_cnt >= SAFE_LIMIT:
                _logger.error("too many msg in buffer!")
                self.out_queue.put(self.buffer.copy())
                self.buffer.clear()
                break
            if len(self.buffer) < BundleHeader.struct_size:
                # _logger("not enough for header")
                break
            header = BundleHeader.from_buffer_copy(self.buffer)
            if header.magic0 != MAGIC_NUMBER and header.magic0 and header.magic1 and header.magic2 and header.magic3:
                _logger.error("Invalid magic in header:", header.get_data())
                self.reset_buffer()
                continue
            if not header.length:
                _logger.error("Invalid header length:", header.get_data())
                self.reset_buffer()
                continue
            if header.length > len(self.buffer):
                # _logger("not enough for full")
                break
            try:
                self.out_queue.put(unpack_message(self.buffer[:header.length]))
            except Exception as e:
                _logger.error(f"Error in unpack message:{e}\n{format_exc()}")
                self.reset_buffer()
                continue
            del self.buffer[:header.length]
            # _logger("msg put")
        return self.get()

    def get(self):
        try:
            return self.out_queue.get(False)
        except QueueEmpty:
            pass

    def reset_buffer(self):
        try:
            idx = self.buffer.index(MAGIC_NUMBER_BYTES, 1)
        except ValueError:
            self.out_queue.put(self.buffer.copy())
            self.buffer.clear()
        else:
            self.out_queue.put(self.buffer[:idx])
            del self.buffer[:idx]


class UnpackError(Exception): pass


class PackError(Exception): pass


def unpack_message(data: bytearray) -> unpacked_messages:
    bundle_header = BundleHeader.from_buffer(data)
    if bundle_header.encoding == 0x0000 or bundle_header.encoding == 0x0001:
        raw_messages = data[BundleHeader.struct_size:bundle_header.length]
    elif bundle_header.encoding == 0x0101 or bundle_header.encoding == 0x0100:
        raw_messages = bytearray(decompress(data[BundleHeader.struct_size + 2:bundle_header.length], wbits=-MAX_WBITS))
    else:
        raise UnpackError(f"unknown encoding type:{bundle_header.encoding:#x}")
    messages = []
    msg_offset = 0
    for i in range(bundle_header.msg_count):
        msg_length = int.from_bytes(raw_messages[msg_offset:msg_offset + 4], byteorder='little')
        messages.append(raw_messages[msg_offset:msg_offset + msg_length])
        msg_offset += msg_length
    return bundle_header, messages


def pack_message(bundle_header: BundleHeader, messages: Iterable[bytearray]) -> bytearray:
    raw_message = bytearray()
    cnt = 0
    for message in messages:
        if message:
            raw_message += message
            cnt += 1
    if not cnt: return raw_message
    if bundle_header.encoding == 0x0000 or bundle_header.encoding == 0x0001:
        compress_messages = raw_message
    elif bundle_header.encoding == 0x0101 or bundle_header.encoding == 0x0100:
        compress_messages = compress(raw_message)
    else:
        raise PackError(f"unknown encoding type:{bundle_header.encoding:#x}")

    bundle_header.msg_count = cnt
    bundle_header.length = bundle_header.struct_size + len(compress_messages)
    return bytearray(bundle_header) + compress_messages

    # bundle_header.encoding = 0
    # bundle_header.msg_count = cnt
    # bundle_header.length = bundle_header.struct_size + len(raw_message)
    # return bytearray(bundle_header) + raw_message

