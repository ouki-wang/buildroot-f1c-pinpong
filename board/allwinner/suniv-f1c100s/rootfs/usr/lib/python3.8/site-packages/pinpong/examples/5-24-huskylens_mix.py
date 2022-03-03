# -*- coding: utf-8 -*-

#实验效果：
# 将一些常用的哈士奇API集成在一个代码中。
# 切换到标签识别功能，对准标签后录入ID，
# 输入e或exit退出
# 输入f或forget遗忘
# 输入s或者switch根据ID来切换算法。（等待5s后会切换回标签识别）
# 

#接线：使用windows或linux电脑连接一块arduino主控板，哈士奇接到I2C口SCL SDA
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_huskylens import Huskylens

Board("uno").begin()  #初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("uno","COM36").begin()  #windows下指定端口初始化
#Board("uno","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("uno","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

husky = Huskylens()

print("切换至标签识别模式...")
husky.command_request_algorthim("ALGORITHM_TAG_RECOGNITION")
time.sleep(.5)

id_list = []

while True:
    print("请对准一个标签，并输入id（输入e退出,输入f遗忘已学习的ID）:")
    v = input() 
    if v == 'e':
        break
    elif v == 'f':
        husky.command_request_forget()
        time.sleep(2)
        print("遗忘已学习的ID")
    elif v == 's':
        while True:
            # 获取数据
            data = husky.command_request()
            if (data):
                num_of_objects = int(len(data)/5)
                for i in range(num_of_objects):
                    #解析出ID
                    ID = data[5*i+4]
                    print("ID:",ID)
                    #当ID等于xx,切换至人脸识别
                    if ID == id_list[0]:
                        print("获取tag ID{}".format(ID))
                        print("切换至人脸识别算法...")
                        husky.command_request_algorthim("ALGORITHM_FACE_RECOGNITION")
                        time.sleep(5)
                        print("根据需求，添加人脸识别的相关代码，比如学习一次，获取数据等")
                        # 自定义代码xxx
                        #
                        #
                        #
                        # 切换回标签识别
                        print("切换回标签识别算法...")
                        husky.command_request_algorthim("ALGORITHM_TAG_RECOGNITION")
                        time.sleep(.5)
                        break
                    #当ID等于xx,切换至人脸识别
                    elif ID == id_list[1]:
                        print("获取tag ID{}".format(ID))
                        print("切换至物体追踪算法...")
                        husky.command_request_algorthim("ALGORITHM_OBJECT_TRACKING")
                        time.sleep(5)
                        print("根据需求，添加物体追踪的相关代码，比如学习一次，获取数据等")

                        # 自定义代码xxx
                        #
                        #
                        #
                        #切换回标签识别
                        print("切换回标签识别算法...")
                        husky.command_request_algorthim("ALGORITHM_TAG_RECOGNITION")
                        time.sleep(.5)
                        break
    else:
        print("已学习标签ID{}".format(v))
        tag_id = int(v)
        id_list.append(tag_id)
        husky.command_request_learn_once(tag_id)
        time.sleep(2)



