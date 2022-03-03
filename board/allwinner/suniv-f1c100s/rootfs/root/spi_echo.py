# -*- coding: utf-8 -*-
#短接PE8 和 PE10 将看到SPI回环传输效果
import spidev
import time

spi=spidev.SpiDev()
spi.open(1,0)

while True:
  ret = spi.xfer([1,2,3,4,5])
  print(ret)
  time.sleep(1)
