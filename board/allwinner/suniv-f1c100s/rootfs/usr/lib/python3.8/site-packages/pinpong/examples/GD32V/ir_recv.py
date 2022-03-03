# -*- coding: utf-8 -*-
#实验效果：展示红外接收功能
#接线：uno支持
import sys
import time
from pinpong.board import Board,IRRecv,Pin

Board("GD32V").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()  #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化


def ir_recv3(data):
  print("------Receiving IR Code--------")
  print(hex(data))

#ir2 = IRRecv(Pin(Pin.P0))
ir3 = IRRecv(Pin(Pin.P22),ir_recv3)

while(1):
#  v = ir2.read()
#  if v:
#    print("------Pin2--------")
#    print(v)
  time.sleep(0.1)