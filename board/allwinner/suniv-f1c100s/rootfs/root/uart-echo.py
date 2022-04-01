#usr/bin/python3
# -*- coding: utf-8 -*-

import serial
import time
 
ser = serial.Serial('/dev/ttyS2', 115200, timeout=3)
 
ser.write("dfrobot".encode('utf-8'))
time.sleep(1)
ret = ser.read(30);
print(ret)

