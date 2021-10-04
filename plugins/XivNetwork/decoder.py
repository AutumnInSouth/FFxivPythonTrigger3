from queue import Queue
from struct import pack

from FFxivPythonTrigger.logger import Logger
from .base_struct import FFXIVBundleHeader

SAFE_LIMIT = 100
MAGIC_NUMBER = 0x41a05252
MAGIC_NUMBER_BYTES = pack('I', MAGIC_NUMBER)
_logger = Logger("XivNetwork/Decoder")


def reset_buffer(buffer: bytearray):
    try:
        idx = buffer.index(MAGIC_NUMBER_BYTES, 1)
    except ValueError:
        buffer.clear()
    else:
        del buffer[:idx]


def process_hook_msg(buffer: bytearray, in_queue: Queue[bytearray], out_queue: Queue[bytearray]):
    while True:
        buffer.extend(in_queue.get())
        msg_cnt = 0
        while buffer:
            msg_cnt += 1
            if msg_cnt >= SAFE_LIMIT:
                _logger.error("too many msg in buffer!")
                buffer.clear()
                break
            if len(buffer) < FFXIVBundleHeader.struct_size:
                break
            header = FFXIVBundleHeader.from_buffer(buffer[:FFXIVBundleHeader.struct_size])
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
            out_queue.put(buffer[:header.length])
            del buffer[:header.length]
        out_queue.put(bytearray())
