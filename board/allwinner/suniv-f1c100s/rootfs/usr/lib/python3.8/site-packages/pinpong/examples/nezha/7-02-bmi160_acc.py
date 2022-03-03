# -*- coding: utf-8 -*-

#Nezha
#实验效果：使用BMI160传感器读取三轴加速度和陀螺仪值


import time
from pinpong.board import Board
from pinpong.libs.dfrobot_bmi160 import BMI160

Board("nezha").begin()

bmi = BMI160()

bmi.begin(bmi.Acc)

while True:
  GyrX = bmi.getGyrX()
  AccX = bmi.getAccX()
  GyrY = bmi.getGyrY()
  AccY = bmi.getAccY()
  GyrZ = bmi.getGyrZ()
  AccZ = bmi.getAccZ()
  print("\n--------------------------------")
  print("AccX=%f, AccY=%f, AccZ=%f"%(AccX,AccY,AccZ))
  print("GyrX=%f, GyrY=%f, GyrZ=%f"%(GyrX,GyrY,GyrZ))
  time.sleep(0.5)