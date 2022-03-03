# -*- coding: utf-8 -*-

#实验效果：使用按钮控制arduino UNO板载亮灭
#接线：使用windows或linux电脑连接一块arduino主控板，主控板D8接一个按钮模块
import time
from pinpong.board import Board,Pin

Board("GD32V").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()   #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

btn = Pin(Pin.P0, Pin.IN) #引脚初始化为电平输入

while True:
  v = btn.value()  #读取引脚电平
  print(v)  #终端打印读取的电平状态
  time.sleep(0.1)
