# -*- coding: utf-8 -*-

import time
from pinpong.board import Board,Pin,WIFI
from pinpong.libs.dfrobot_ssd1306 import SSD1306_I2C #导入ssd1306库

Board("PinPong Board").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别

oled=SSD1306_I2C(width=128, height=64) #初始化屏幕，传入屏幕像素点数
obj = WIFI()

ssid = "dfrobotOffice"                      #wifi名
password = "dfrobot2011"                    #wifi密码

obj.set_ssid(ssid)                          #设置wifi名
obj.set_password(password)                  #设置wifi密码
obj.connect_wifi()                          #开始连接
print("Waiting for WIFI connection...")
time.sleep(5)

while True:
  ip,port = obj.get_ip_port()
  if ip != None:
    print("ip: {} port: {}".format(ip, port))#打印ip地址和port
    break
  time.sleep(1)

ip = "ip:" + str(ip)
port = "port:"+str(port)
oled.text(ip,0,10) #指定位置显示文字
oled.text(port,0,30)
oled.show()  #显示生效
