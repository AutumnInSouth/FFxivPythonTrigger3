from ctypes import *
from FFxivPythonTrigger import *
from FFxivPythonTrigger.memory import *
from FFxivPythonTrigger.memory.struct_factory import *
from FFxivPythonTrigger.saint_coinach import realm
from FFxivPythonTrigger.text_pattern import find_signature_point, find_signature_address
from XivMemory.se_string.messages import *


s="""
《诗学的用处》
亚拉戈诗学神典石可以用于兑换50级开始的整十级装备
属性足以使用一个等级段推荐可以兑换后第一时间更新
完成50级主线<q quest_id=66060>后开放<i item_id=8933>
兑换地点：<p map_id=25 map_x=22.7 map_y=6.7 z=0><p map_id=12 map_x=9.9 map_y=11.4 z=0>
                   <p map_id=2 map_x=11.9 map_y=12.3 z=0><p map_id=13 map_x=9.1 map_y=8.3 z=0>
完成58级主线<quest quest_id=67191>后开放<i item_id=16327>
兑换地点：<p map_id=257 map_x=5.8 map_y=5.3 z=0><p map_id=218 map_x=10.5 map_y=11.8 z=0>
完成70级主线<quest quest_id=68089>后开放<i item_id=23472>
兑换地点：<p map_id=370 map_x=12.2 map_y=10.8 z=0><p map_id=366 map_x=138.5 map_y=11.6 z=0>
版本满级时开始使用新点数，而非诗学
如果诗学溢出可兑换副职装备以作备用
"""

channel = '/cwl1'

for line in s.strip().split('\n'):
    plugins.XivMemory.calls.do_text_command(f"{channel} {line}")
