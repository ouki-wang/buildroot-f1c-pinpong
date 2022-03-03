# -*- coding: utf-8 -*-

import time
from pinpong.board import Board,Pin
from pinpong.extension.GD32V import *

Board("GD32V").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()   #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

def btn_rasing_handler(pin):#中断事件回调函数
  print("---rising---")
  print("pin = ", pin)

def btn_falling_handler(pin):#中断事件回调函数
  print("---falling---")
  print("pin = ", pin)

def btn_both_handler(pin):#中断事件回调函数
  print("\n--both---")
  print("pin = ", pin)

button_a.irq(trigger=Pin.IRQ_RISING, handler = btn_rasing_handler)
#button_a.irq(trigger=Pin.IRQ_FALLING, handler=btn_falling_handler)
#button_a.irq(trigger=Pin.IRQ_RISING+Pin.IRQ_FALLING, handler=btn_both_handler)

#button_b.irq(trigger=Pin.IRQ_RISING, handler = btn_rasing_handler)
button_b.irq(trigger=Pin.IRQ_FALLING, handler=btn_falling_handler)
#button_b.irq(trigger=Pin.IRQ_RISING+Pin.IRQ_FALLING, handler=btn_both_handler)

while True:
  print(button_a.is_pressed())                    #按键A是否按下
  print(button_b.is_pressed())                    #按键B是否按下
  print(light.read())                             #读取环境光强度
  print(accelerometer.get_x())                    #读取加速度X的值
  print(accelerometer.get_y())                    #读取加速度Y的值
  print(accelerometer.get_z())                    #读取加速度Z的值

  print(gyroscope.get_x())                        #读取陀螺仪X的值
  print(gyroscope.get_y())                        #读取陀螺仪Y的值
  print(gyroscope.get_z())                        #读取陀螺仪Z的值

  print("------------------")
  time.sleep(1)
