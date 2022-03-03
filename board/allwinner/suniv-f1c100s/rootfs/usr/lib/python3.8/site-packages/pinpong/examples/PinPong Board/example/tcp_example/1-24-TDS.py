# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin
from pinpong.libs.dfrobot_TDS import TDS

ip = "192.168.0.15"
port = 8081

Board(ip, port)

tds = TDS(Pin.A0)

while True:
    tds_value = tds.get_value()
    print("TDS Value: %d ppm" % tds_value)
    time.sleep(1)


  