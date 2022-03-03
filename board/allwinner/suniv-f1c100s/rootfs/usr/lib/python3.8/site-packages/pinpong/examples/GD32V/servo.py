# -*- coding: utf-8 -*-

#实验效果：舵机控制
#接线：使用windows或linux电脑连接一块arduino主控板，D4连接一个舵机
import time
from pinpong.board import Board,Pin,Servo

Board("GD32V").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()  #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

s1 = Servo(Pin(Pin.P10)) #将Pin传入Servo中初始化舵机引脚,支持P0 P3 P8 P9 P10 P16  P21 P22 P23

while True:
  s1.angle(0) #控制舵机转到0度位置
  print("0")
  time.sleep(1)

  s1.angle(90) #控制舵机转到90度位置
  print("90")
  time.sleep(1)

  s1.angle(180) #控制舵机转到180度位置
  print("180")
  time.sleep(1)

  s1.angle(90) #控制舵机转到90度位置
  print("90")
  time.sleep(1)
