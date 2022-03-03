# -*- coding: utf-8 -*-

#实验效果：I2C obloq
#接线：使用windows或linux电脑连接一块handpy主控板，obloq接到I2C口SCL及SDA
import time
from pinpong.board import Board
from pinpong.libs.microbit_motor import Microbit_Motor #导入ssd1306库

Board("handpy").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("handpy","COM36").begin()  #windows下指定端口初始化
#Board("handpy","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("handpy","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

motorbit = Microbit_Motor()

while True:
   #舵机引脚S1-S8,角度范围0-180
   motorbit.servo(motorbit.S8, 0)
   time.sleep(1)
   motorbit.servo(motorbit.S8, 90)
   time.sleep(1)
   motorbit.servo(motorbit.S8, 180)
   time.sleep(1)
   motorbit.servo(motorbit.S8, 90)
   time.sleep(1)
