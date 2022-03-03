# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_mpu6050 import MPU6050

ip = "192.168.1.106"
port = 8081

Board(ip, port)

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