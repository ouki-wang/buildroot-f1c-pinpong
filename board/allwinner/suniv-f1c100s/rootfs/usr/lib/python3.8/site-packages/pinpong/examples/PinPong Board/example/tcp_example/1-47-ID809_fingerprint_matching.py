# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin
from pinpong.libs.dfrobot_ID809 import ID809

ip = "192.168.1.116"
port = 8081

Board(ip, port)

fingerprint = ID809()

while fingerprint.isConnected() == False:
    print("Communication with device failed, please check connection")
    time.sleep(1)

while True:
#   ctrlLED参数1:<LEDMode>
#   Breathing   FastBlink   KeepsOn    NormalClose
#   FadeIn      FadeOut     SlowBlink   
#   ctrlLED参数2:<LEDColor>
#   LEDGreen  LEDRed      LEDYellow   LEDBlue
#   LEDCyan   LEDMagenta  LEDWhite
#   ctrlLED参数2参数3:<呼吸、闪烁次数> 0表示一直呼吸、闪烁，
#   该参数仅eBreathing、FastBlink、SlowBlink模式下有效
    fingerprint.ctrlLED(fingerprint.Breathing, fingerprint.LEDBlue, 0)
    print("请按下手指")
    if fingerprint.collection_fingerprint(10) != fingerprint.ERR_ID809:
        fingerprint.ctrlLED(fingerprint.FastBlink, fingerprint.LEDYellow, 3)
        print("采集成功")
        print("请松开手指")
        while fingerprint.detect_finger():pass
        ret = fingerprint.search()   #将采集到的指纹与指定编号指纹对比,成功返回指纹编号(1-80)，失败返回0
        if ret != 0:
        #设置指纹灯环为绿色常亮
            fingerprint.ctrlLED(fingerprint.KeepsOn, fingerprint.LEDGreen, 0)
            print("匹配成功,ID = {}".format(ret))
        else:
            print("匹配失败")
    else:
        print("采集失败")
    print("-----------------------------")
    time.sleep(1)
        