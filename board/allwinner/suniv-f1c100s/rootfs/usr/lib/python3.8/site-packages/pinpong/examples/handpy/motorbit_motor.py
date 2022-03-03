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
#电机有M1,M2,M3,M4, CW代表正转，CCW代表反转，255是速度，范围0-255
motorbit.motor_run(motorbit.M3, motorbit.CW, 255)
time.sleep(5)
motorbit.motor_stop(motorbit.M3)



