 # -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_mcp4725 import MCP4725

ip = "192.168.1.116"
port = 8081

Board(ip, port)

REF_VOLTAGE    = 5000
OUTPUT_VOLTAGE = 1000
DAC = MCP4725()

#MCP4725A0_IIC_Address0 -->0x60
#MCP4725A0_IIC_Address1 -->0x61

DAC.init(DAC.MCP4725A0_IIC_Address0, REF_VOLTAGE)

while True:
    print("DFRobot_MCP4725 write to EEPROM and output: {} mV".format(OUTPUT_VOLTAGE))
    DAC.output_voltage_EEPROM(OUTPUT_VOLTAGE)
    time.sleep(0.2)