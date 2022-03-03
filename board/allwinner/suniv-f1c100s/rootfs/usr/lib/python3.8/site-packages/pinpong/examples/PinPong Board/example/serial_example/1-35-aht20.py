# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_aht20 import AHT20

Board("PinPong board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("PinPong Board","COM36").begin()   #windows下指定端口初始化
#Board("PinPong Board","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("PinPong Board","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

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