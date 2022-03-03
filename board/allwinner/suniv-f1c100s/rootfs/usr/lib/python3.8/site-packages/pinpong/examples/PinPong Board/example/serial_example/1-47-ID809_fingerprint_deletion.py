# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin
from pinpong.libs.dfrobot_ID809 import ID809

Board("PinPong board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("PinPong board","COM36").begin()  #windows下指定端口初始化
#Board("PinPong board","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("PinPong board","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

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
    print("请按下需要删除指纹的手指")
    if fingerprint.collection_fingerprint(10) != fingerprint.ERR_ID809:
        ret = fingerprint.search()
        if ret != 0:
            fingerprint.del_fingerprint(ret)   #删除要删除得ID
#            fingerprint.del_fingerprint(fingerprint.DELALL)   #删除全部ID
            print("删除成功,ID = {}".format(ret))
        else:
            print("指纹未注册")
    else:
        print("采集失败")
        fingerprint.ctrlLED(fingerprint.KeepsOn, fingerprint.LEDRed, 0)
    print("请松开手指")
    while(fingerprint.detect_finger()):pass
    print("-------------------------")
    time.sleep(1)