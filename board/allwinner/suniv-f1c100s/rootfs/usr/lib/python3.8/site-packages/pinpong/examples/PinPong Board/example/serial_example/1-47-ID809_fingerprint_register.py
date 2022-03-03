# -*- coding: utf-8 -*-
import time
from pinpong.board import Board,Pin
from pinpong.libs.dfrobot_ID809 import ID809

Board("PinPong board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("PinPong board","COM36").begin()  #windows下指定端口初始化
#Board("PinPong board","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("PinPong board","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

fingerprint = ID809()

COLLECT_NUMBER = 3

while fingerprint.isConnected() == False:
    print("Communication with device failed, please check connection")
    time.sleep(1)

while True:
    print("-----------------------------")
    ID = fingerprint.get_emptyID()                                       #获取一个空ID
    print("未注册编号,ID={}".format(ID))

#   ctrlLED参数1:<LEDMode>
#   Breathing   FastBlink   KeepsOn    NormalClose
#   FadeIn      FadeOut     SlowBlink   
#   ctrlLED参数2:<LEDColor>
#   LEDGreen  LEDRed      LEDYellow   LEDBlue
#   LEDCyan   LEDMagenta  LEDWhite
#   ctrlLED参数2参数3:<呼吸、闪烁次数> 0表示一直呼吸、闪烁，
#   该参数仅eBreathing、FastBlink、SlowBlink模式下有效
    i = 0
    while i < COLLECT_NUMBER:
        fingerprint.ctrlLED(fingerprint.Breathing, fingerprint.LEDBlue, 0)
        print("正在进行第{}次指纹采集".format(i+1))
        print("请按下手指")
#采集指纹图像，超过10S没按下手指则采集超时，如果timeout=0，关闭采集超时功能,如果获取成功返回0，否则返回ERR_ID809
        if fingerprint.collection_fingerprint(10) != fingerprint.ERR_ID809:      
            fingerprint.ctrlLED(fingerprint.FastBlink, fingerprint.LEDYellow, 3) #设置指纹灯环为黄色快闪3次
            print("采集成功")
            i += 1
        else:
            print("采集失败")
        print("请松开手指")
        while fingerprint.detect_finger():pass
    if fingerprint.store_fingerprint(ID) != fingerprint.ERR_ID809:      #将指纹信息保存到一个未注册的编号中
        print("保存成功，ID={}".format(ID))
        fingerprint.ctrlLED(fingerprint.KeepsOn, fingerprint.LEDGreen, 0)  #设置指纹灯环为绿色常亮
        time.sleep(1)
        fingerprint.ctrlLED(fingerprint.NormalClose, fingerprint.LEDBlue, 0)#关闭指纹灯环
        time.sleep(1)
    else:
        print("保存失败")
    
    