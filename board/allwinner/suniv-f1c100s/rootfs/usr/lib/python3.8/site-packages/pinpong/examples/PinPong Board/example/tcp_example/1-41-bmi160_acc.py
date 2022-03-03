# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_bmi160 import BMI160

ip = "192.168.1.116"
port = 8081

Board(ip, port)

bmi = BMI160()

bmi.begin(bmi.Acc)

while True:
  GyrX = bmi.getGyrX()
  AccX = bmi.getAccX()
  GyrY = bmi.getGyrY()
  AccY = bmi.getAccY()
  GyrZ = bmi.getGyrZ()
  AccZ = bmi.getAccZ()
  print("{}  {}  {}  {}  {}  {}".format(GyrX, GyrY, GyrZ, AccX, AccY, AccZ))
  time.sleep(0.5)