# -*- coding: utf-8 -*-

#Nezha
#实验效果：扫描所有外接IIC设备的地址

import time
from pinpong.board import Board,I2C

Board("F1C").begin()

iic=I2C(bus_num=1)
ret=iic.scan()
print(ret)
