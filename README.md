# modbus
Modbus utility programs

## reader/modbus_reader.py
Read modbus register by modbus/tcp. Support only function code 0x03 and 0x04.

Input parameters in either hex (with 0x, e.g 0x0fa2) or dec (e.g 4002).

### Usage

`$python modbus_reader.py [ip address]`

### Example
Normal
```
$python modbus_reader.py 192.168.1.101

Enter Modbus Params in [0xnn (Hex)] or [nn (Dec)]
 Unit Identifier: 0x2
 Function Code: 0x4
 Start Register: 0x290
 Num of Registers: 0x4

TX: b'000000000006020402900004'
RX: b'00000000000b02040803eb020802080000'

Modbus Application Data Unit (ADU)
 Transaction Identifier : 0
 Protocol Identifier : 0
 Length : 11
 Unit Identifier : 2
 Function Code : 4
 Byte Count : 8

Register: Value
  #0x290 : 0x03eb : 1003
  #0x291 : 0x0208 : 520
  #0x292 : 0x0208 : 520
  #0x293 : 0x0000 : 0

Done
```
Error
```
$python modbus_reader.py 192.168.1.101

Enter Modbus Params in [0xnn (Hex)] or [nn (Dec)]
 Unit Identifier: 4
 Function Code: 4
 Start Register: 656
 Num of Registers: 4

TX: b'000000000006040402900004'
RX: b'00000000000304840a'

Modbus Application Data Unit (ADU)
 Transaction Identifier : 0
 Protocol Identifier : 0
 Length : 3
 Unit Identifier : 4
 Error Code     : 0x84 : 132
 Exception Code : 0x0a : 10

Done
```


