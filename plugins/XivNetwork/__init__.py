from FFxivPythonTrigger import PluginBase


class XivNetwork(PluginBase):
    name = ""

    def is_zone_socket(self, socket: int) -> bool:
        pass


"""
<?xml version="1.0" encoding="utf-8"?>
<CheatTable>
  <CheatEntries>
    <CheatEntry>
      <ID>0</ID>
      <Description>"zone socket"</Description>
      <LastState Value="2627302936" RealAddress="2349BF04070"/>
      <VariableType>4 Bytes</VariableType>
      <Address>"ffxiv_dx11.exe"+01D6B3C8</Address>
      <Offsets>
        <Offset>0</Offset>
        <Offset>368</Offset>
      </Offsets>
    </CheatEntry>
    <CheatEntry>
      <ID>1</ID>
      <Description>"chat result"</Description>
      <LastState Value="2627302936" RealAddress="2349BF04210"/>
      <VariableType>4 Bytes</VariableType>
      <Address>"ffxiv_dx11.exe"+01D6B3C8</Address>
      <Offsets>
        <Offset>0</Offset>
        <Offset>10</Offset>
        <Offset>10</Offset>
        <Offset>8</Offset>
        <Offset>130</Offset>
        <Offset>368</Offset>
      </Offsets>
    </CheatEntry>
  </CheatEntries>
</CheatTable>
"""
