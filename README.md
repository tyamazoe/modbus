# modbus
Modbus utility programs

## reader/modbus_reader.py
Read modbus register by modbus/tcp. Support only function code 0x03 and 0x04.

### Usage

`$python modbus_reader.py [ip address]`

### Example
Normal
```
$python modbus_reader.py 192.168.1.101

Enter Modbus Params
 Unit Identifier (Hex): 2
 Function Code (Hex): 4
 Start Register (Hex) : 290
 Num of Registers (Hex) : 4

TX: b'000000000006020402900004'
RX: b'00000000000b02040803f2020a020a0000'

Modbus Application Data Unit (ADU)
 Transaction Identifier : 0
 Protocol Identifier : 0
 Length : 11
 Unit Identifier : 2
 Function Code : 4
 Byte Count : 8

Register: Value
 #0x290 : 0x03f2 : 1010
 #0x291 : 0x020a : 522
 #0x292 : 0x020a : 522
 #0x293 : 0x0000 : 0
Done
```
Error
```
$python modbus_reader.py 192.168.1.101
Enter Modbus Params
 Unit Identifier (Hex): 4
 Function Code (Hex): 4
 Start Register (Hex) : 290
 Num of Registers (Hex) : 10

TX: b'000000000006040402900010'
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


