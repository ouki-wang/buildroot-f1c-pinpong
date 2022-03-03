# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_mpu6050 import MPU6050

Board("PinPong Board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("PinPong Board","COM36").begin()   #windows下指定端口初始化
#Board("PinPong Board","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("PinPong Board","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

accelgyro = MPU6050()

accelgyro.init()
 
if accelgyro.connection():
    print("MPU6050 connection successful")
else: 
    print("MPU6050 connection failed")

while True:
    buf = accelgyro.get_motion6()
    print("ax:{} ay:{} az:{} gx:{} gy:{} gz:{}".format(buf[0], buf[1], buf[2],buf[3],buf[4],buf[5]))
    time.sleep(0.3)