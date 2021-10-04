from queue import Queue
from struct import pack
from traceback import format_exc
from typing import Iterable, Tuple, List, Optional
from zlib import decompress, MAX_WBITS, compress

from FFxivPythonTrigger.logger import Logger
from .base_struct import BundleHeader, MessageHeader

SAFE_LIMIT = 100
MAGIC_NUMBER = 0x41a05252
MAGIC_NUMBER_BYTES = pack('I', MAGIC_NUMBER)
_logger = Logger("XivNetwork/Decoder")
unpacked_messages = Tuple[BundleHeader, List[Tuple[MessageHeader, bytearray]]]


def reset_buffer(buffer: bytearray):
    try:
        idx = buffer.index(MAGIC_NUMBER_BYTES, 1)
    except ValueError:
        buffer.clear()
    else:
        del buffer[:idx]


def process_hook_msg(buffer: bytearray, in_queue: Queue[bytearray], out_queue: Queue[Optional[unpacked_messages]]):
    while True:
        buffer.extend(in_queue.get())
        msg_cnt = 0
        while buffer:
            msg_cnt += 1
            if msg_cnt >= SAFE_LIMIT:
                _logger.error("too many msg in buffer!")
                buffer.clear()
                break
            if len(buffer) < BundleHeader.struct_size:
                break
            header = BundleHeader.from_buffer(buffer[:BundleHeader.struct_size])
            if header.magic0 != MAGIC_NUMBER and header.magic0 and header.magic1 and header.magic2 and header.magic3:
                _logger.error("Invalid magic in header:", header.get_data())
                reset_buffer(buffer)
                continue
            if not header.length:
                _logger.error("Invalid header length:", header.get_data())
                reset_buffer(buffer)
                continue
            if header.length > len(buffer):
                break
            try:
                out_queue.put(unpack_message(buffer[:header.length]))
            except Exception as e:
                _logger.error(f"Error in unpack message:{e}\n{format_exc()}")
                reset_buffer(buffer)
                continue
            del buffer[:header.length]
        out_queue.put(None)


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
        message_header = MessageHeader.from_buffer(raw_messages, offset=msg_offset)
        messages.append((message_header, raw_messages[msg_offset:msg_offset + message_header.msg_length]))
        msg_offset += message_header.msg_length
    return bundle_header, messages


def pack_message(bundle_header: BundleHeader, messages: Iterable[Tuple[MessageHeader, bytearray]]) -> bytearray:
    raw_message = bytearray()
    cnt = 0
    for message_header, message in messages:
        raw_message += bytearray(message_header) + message
        cnt += 1
    if not cnt: return raw_message
    if bundle_header.encoding == 0x0000 or bundle_header.encoding == 0x0001:
        compress_messages = raw_message
    elif bundle_header.encoding == 0x0101 or bundle_header.encoding == 0x0100:
        compress_messages = compress(raw_message)[2:]
    else:
        raise PackError(f"unknown encoding type:{bundle_header.encoding:#x}")

    bundle_header.msg_count = cnt
    bundle_header.length = bundle_header.struct_size + len(compress_messages)
    return bytearray(bundle_header) + compress_messages
