# -*- coding: utf-8 -*-
#
# Modbus/TCP writer
#
import socket
import struct
import time
import traceback
import codecs
import sys

TARGET_IP = '192.168.1.99'
try:
    TARGET_IP = sys.argv[1]
except IndexError:
    pass # use defaults

TARGET_PORT = 502
buffer_size = 0
#SUPPORTED_FC = (0x05, 0x06)


def get_param(msg):
    param = input(msg)
    hex_dec = 16 if "0x" in param.lower() else 10
    return int(param, hex_dec)

try:
    print("\nEnter Modbus Params in [0xnn (Hex)] or [nn (Dec)]")
    unitId = get_param(" Unit Identifier: ")
    functionCode = get_param(" Function Code: ")
    #if functionCode not in  SUPPORTED_FC:
    #    raise Exception("FC only support {}".format(SUPPORTED_FC))
    if functionCode == 0x05:
        startRegister = get_param(" Start Register: ")
        pack_data = 0xff00 if get_param(" On(1) or Off(0):") == 1 else 0x0000
        numRegister = 2
    else:
        #raise Exception("FC only support {}".format(SUPPORTED_FC))
        raise Exception("FC only support  0x05")

    # Send request
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TARGET_IP, TARGET_PORT))
    req = struct.pack('>3H 2B 2H', 0, 0, 6, unitId, functionCode, startRegister, pack_data)
    sock.send(req)

    # Receive response
    buffer_size = len(req)
    res = sock.recv(buffer_size)
    print("\nTX: {0}".format(codecs.encode(req, 'hex_codec')))
    print("RX: {0}".format(codecs.encode(res, 'hex_codec')))

    if res == req:
        print("\nOK, write completed.")
    else:
        # error response
        s = struct.Struct('>3H 3B')
        data = s.unpack(res)
        print("\nModbus Application Data Unit (ADU)")
        print(" Transaction Identifier : %s" %data[0])
        print(" Protocol Identifier : %s" %data[1])
        print(" Length : %s" %data[2])
        print(" Unit Identifier : %s" %data[3])
        print(" Error Code     : 0x{0:02x} : {0}".format(data[4]))
        print(" Exception Code : 0x{0:02x} : {0}".format(data[5]))

    sock.close()
except:
    print(traceback.format_exc())
finally:
    print("\nDone")
