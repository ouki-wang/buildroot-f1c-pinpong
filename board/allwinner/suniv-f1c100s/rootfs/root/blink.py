# -*- coding: utf-8 -*-

#RPi, F1C  and PythonBoard 
#实验效果：控制板载LED灯一秒闪烁一次

import time
from pinpong.board import Board,Pin

Board("F1C").begin()
#135-PE7  136-PE8 137-PE9 138-PE10 不可用
led = Pin(12, Pin.OUT) #RPi引脚初始化为电平输出

while True:
  led.value(1) #输出高电平
  print("1") #终端打印信息
  time.sleep(1) #等待1秒 保持状态

  led.value(0) #输出低电平
  print("0") #终端打印信息
  time.sleep(1) #等待1秒 保持状态
