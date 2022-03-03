# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_Ozone import Ozone

ip = "192.168.1.116"
port = 8081

Board(ip, port)

oz = Ozone(0x73)
#设置模式主动或者被动模式, MEASURE_MODE_AUTOMATIC,MEASURE_MODE_PASSIVE
oz.set_mode(oz.MEASURE_MODE_AUTOMATIC)
COLLECT_NUMBER = 20

while True:
    value = oz.read_Ozone_data(COLLECT_NUMBER)
    print("Ozone concentration is {} PPB".format(value))
    time.sleep(1)