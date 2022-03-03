# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_mcp4725 import MCP4725

Board("uno").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("uno","COM36").begin()  #windows下指定端口初始化
#Board("uno","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("uno","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

REF_VOLTAGE    = 5000
OUTPUT_VOLTAGE = 5000
DAC = MCP4725()

#MCP4725A0_IIC_Address0 -->0x60
#MCP4725A0_IIC_Address1 -->0x61

DAC.init(DAC.MCP4725A0_IIC_Address0, REF_VOLTAGE)

while True:
    print("DFRobot_MCP4725 output: {} mV".format(OUTPUT_VOLTAGE))
    DAC.output_voltage(OUTPUT_VOLTAGE)
    time.sleep(0.5)