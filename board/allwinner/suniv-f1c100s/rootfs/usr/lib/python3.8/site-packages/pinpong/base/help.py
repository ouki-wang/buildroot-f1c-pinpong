# -*- coding: utf-8 -*-
import sys, getopt
import serial
import os
import json
import platform
import serial.tools.list_ports
from pinpong.base.comm import *

def main():
  argc = len(sys.argv)
  cwdpath,_ = os.path.split(os.path.realpath(__file__))

  with open(cwdpath+'/../libs/libs.json', 'r', encoding='UTF-8') as f:
    descs = json.loads(f.read())
  if argc == 1:
    argc = 2
    sys.argv.append("help")
  cmd = sys.argv[1]
  if cmd == "help" and argc == 2:
    printlogo()
    version = sys.version.split(' ')[0]
    plat = platform.platform()
    print("[1]环境信息(Environment information)：Python"+version+"  "+plat+"\n")
    print("[2]文档网址(Document URL)："+"\n")
    print("主站：https://pinpong.readthedocs.io"+"\n")
    print("镜像站：https://pinpong.gitee.io"+"\n")
    print("[3]终端命令(Commands)：")
    print("   pinpong              pinpong库的帮助信息")
    print("   pinpong libs list    pinpong库列表")
    print("   pinpong libs xxx     xxx库的使用方法\n")
    print("[4]串口列表(Serial ports list):")
    plist = list(serial.tools.list_ports.comports())
    for port in plist:
      print("  ",port)
  elif cmd == "libs" and argc == 3:
    arg = sys.argv[2]
    if arg == "list":
      print("\n[-] 库列表(Libs list):")
      items = descs.items()
      for key,_ in items:
        print(str(key).lower())
    else:
      if arg.upper() in descs:
        print("\n[-] 导入方法(How to import?): ")
        print(descs[arg.upper()]["import"])
        print("\n[-] API列表(API list) ")
        print(descs[arg.upper()]["api"])
      else:
        print("[Err] 未知库(Unknown lib): ",arg)
  else:
    print("\n[Err] 未知命令(Unknown command):", sys.argv[1])
    print("\n[-] 支持如下快捷命令(Available commands)")
    print("  pinpong              pinpong库的帮助信息")
    print("  pinpong libs list    当前pinpong库所支持的模块列表")
    print("  pinpong libs xxx     xxx模块的使用方法")
