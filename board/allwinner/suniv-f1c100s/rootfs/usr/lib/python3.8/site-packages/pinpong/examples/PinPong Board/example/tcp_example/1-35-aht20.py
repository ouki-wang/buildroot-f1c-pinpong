# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_aht20 import AHT20

ip = "192.168.1.116"
port = 8081

Board(ip, port)

aht = AHT20()

while True:
    if not aht.wait_flag:
        aht.measure_template_humidity()
    buf = aht.get_template_humidity()
    if buf == -1:
        print("wait!")
    else:
        print("humidity = {} %RH".format(buf[0]))
        print("template = {} ℃".format(buf[1]))
        print("---------------------------")
    time.sleep(0.2)