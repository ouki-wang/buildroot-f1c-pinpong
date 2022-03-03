# -*- coding: utf-8 -*-

import time
from pinpong.board import Board,Pin
from pinpong.extension.microbit import *

Board("microbit").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("microbit","COM36").begin()   #windows下指定端口初始化
#Board("microbit","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("microbit","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

#接口播放音乐：DADADADUM、ENTERTAINER、PRELUDE、ODE、NYAN、RINGTONE、FUNK、BLUES、BIRTHDAY、WEDDING、FUNERAL、PUNCHLINE、BADDY
#CHASE、BA_DING、WAWAWAWAA、JUMP_UP、JUMP_DOWN、POWER_UP、POWER_DOWN
music.play(music.ENTERTAINER, Pin.P0, wait = False)   #后台播放音乐
#music.play(music.DADADADUM, Pin.P0, wait = True)    #播放音乐直到结束
# 音符C/C3、D/D3、E/E3、F/F3、G/G3、A/A3、B/B3、C/C4、D/D4、E/E4、F/F4、G/G4、A/A4、B/B4、C/C5、D/D5、E/E5、F/F5、G/G5、A/A5、B/B5
# C#/C#3、D#/D#3、F#/F#3、G#/G#3、A#/A#3、C#/C#4、D#/D#4、F#/F#4、G#/G#4、A#/A#4、C#/C#5、D#/D#5、F#/F#5、G#/G#5、A#/A#5
#节拍1、0.5、0.25、2、4
#music.play_buzzer(Pin.P0, "F/F3", 2)                   #播放音符
#music.add_tempo(20)                                    #将声音速度增加 x
#music.set_tempo(220)                                   #设置声音速度为 x
#print(music.get_tempo())                               #获取声音速度
#for freq in range(880, 1760, 16):
#    music.pitch(freq, 6)                               #设置频率响多少时间(ms)
