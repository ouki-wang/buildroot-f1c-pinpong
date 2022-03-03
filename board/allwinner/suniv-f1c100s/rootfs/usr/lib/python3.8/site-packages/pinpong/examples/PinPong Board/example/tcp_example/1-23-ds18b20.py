# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin,DS18B20

ip = "192.168.0.15"
port = 8081

Board(ip, port)

ds18b20 = DS18B20(Pin(Pin.D4))

while True:
  temp = ds18b20.temp_c()
  print("temperature = ",temp)
  time.sleep(1)














