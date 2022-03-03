# -*- coding: utf-8 -*-
import time
from pinpong.libs.framebuf import FRAME_BUF
from pinpong.board import gboard,SPI

class ST7789:
  COLOR_NAVY    =  0x000F  #  深蓝色  
  COLOR_DGREEN  =  0x03E0  #  深绿色  
  COLOR_DCYAN   =  0x03EF  #  深青色  
  COLOR_MAROON  =  0x7800  #  深红色  
  COLOR_PURPLE  =  0x780F  #  紫色  
  COLOR_OLIVE   =  0x7BE0  #  橄榄绿  
  COLOR_LGRAY   =  0xC618  #  灰白色
  COLOR_DGRAY   =  0x7BEF  #  深灰色  
  COLOR_BLUE    =  0x001F  #  蓝色    
  COLOR_GREEN   =  0x07E0  #  绿色    
  COLOR_CYAN    =  0x07FF  #  青色  
  COLOR_RED     =  0xF800  #  红色    
  COLOR_MAGENTA =  0xF81F  #  品红    
  COLOR_YELLOW  =  0xFFE0  #  黄色   
  COLOR_BLACK   =  0x0000  #  黑色    
  COLOR_BLUE    =  0x001F  #  蓝色  
  COLOR_GREEN   =  0x07E0  #  绿色 
  COLOR_WHITE   =  0xFFFF  #  白色 

  MERGE   = 0 #混合模式
  REPLACE = 1 #覆盖模式

  FULL    = 0#全局刷新
  PART    = 1#局部刷新

  init_cmds = [
    #flag cmd 最高位为1表示后2位是延时，低7位表示参数的个数
    0x01, 0x01, 0x80, 0, 150,
    0x01, 0x11, 0x80, 0, 120,
    0x01, 0x3A, 1, 0x55,
    0x01, 0x36, 1, 0x00,
    0x01, 0x21, 0,
    0x01, 0x13, 0,
    0x01, 0x29, 0,
    0x00
  ]
  
  _ST7789_COLSET = 0x2A
  _ST7789_RAWSET = 0x2B
  _ST7789_RAMWR  = 0x2C
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.buffer = [[0 for col in range(2)] for row in range(width*height)]#定义一个二维列表
    self.framebuf = FRAME_BUF(self.buffer,self.width,self.height,'RGB565')
    self.set_flush_mode(self.PART)
    self.reset()

  def reset(self):
    offset = 0
    while self.init_cmds[offset]:
      offset += 1
      cmd = self.init_cmds[offset]
      offset += 1
      val = self.init_cmds[offset]
      offset += 1
      argsNum = val & 0x7F
      if val & 0x80:
        duration = self.init_cmds[offset]*255 + self.init_cmds[offset+1]
        time.sleep(duration/1000)
        offset += 2
      self.send_cmd(cmd, self.init_cmds[offset:offset+argsNum])
      offset += argsNum
  
  def show(self):
    buf = []
    self.send_cmd(self._ST7789_COLSET)
    self.send_data16(0)#x起始坐标
    self.send_data16(self.width)#x结束坐标
    self.send_cmd(self._ST7789_RAWSET)
    self.send_data16(0)#y起始坐标
    self.send_data16(self.height)#y结束坐标
    self.send_cmd(self._ST7789_RAMWR)
    for y in range(0,self.height):
      buf += [n for a in self.buffer[(y*self.width):(y*self.width+self.height)] for n in a ]#展开成一维列表
    self.send_buf(buf)

  def flush(self,buf,x1,y1,x2,y2):
    self.send_cmd(self._ST7789_COLSET)
    self.send_data16(x1)#x起始坐标
    self.send_data16(x2)#x结束坐标
    self.send_cmd(self._ST7789_RAWSET)
    self.send_data16(y1)#y起始坐标
    self.send_data16(y2)#y结束坐标
    self.send_cmd(self._ST7789_RAMWR)
    self.send_buf(buf)

  def set_blend_mode(self,mode):
    self.framebuf.set_blend_mode(mode)
  
  def set_flush_mode(self,mode):
    self.framebuf.set_flush_mode(mode)
  
  def set_font(self,font,width,height,kerning,rowledge):
    self.framebuf.set_font(font,width,height,kerning,rowledge)

  def fill(self,color):
    self.framebuf.fill(color,self)

  def text(self,text,x,y,color,mode=True):
    self.framebuf.text(str(text),x,y,color,mode,self)
    
  def rect(self,x1,y1,x2,y2,color):
    self.framebuf.rect(x1,y1,x2,y2,color,self)
  
  def fill_rect(self,x1,y1,x2,y2,color):
    self.framebuf.fill_rect(x1,y1,x2,y2,color,self)
  
  def circle(self,x,y,r,color):
    self.framebuf.circle(x,y,r,color,self)
  
  def fill_circle(self,x,y,r,color):
    self.framebuf.fill_circle(x,y,r,color,self)
  
  def line(self,x1,y1,x2,y2,color):
    self.framebuf.line(x1,y1,x2,y2,color,self)
  
  def picture(self,filename,x,y,size):
    self.framebuf.picture(filename,x,y,size,self)


class ST7789_SPI(ST7789):
  def __init__(self, board=None, width=240, height=240, bus_num=1, device_num=0, dc=None, res=None, cs=None, font="msyh"):
    if board is None:
      board = gboard

    self.board = board
    self.dc=dc
    self.cs=cs
    self.res=res
    self.spi = SPI(bus_num=bus_num,device_num=device_num)
    super().__init__(width, height)
    self.reset()

  def reset(self):
    if self.res:
      self.res.value(1)
    if self.dc:
      self.dc.value(1)
    if self.res:
      self.res.value(0)
      time.sleep(0.2)
      self.res.value(1)
      time.sleep(0.2)
    super().reset()

  def send_cmd(self, cmd, value=None):
    self.dc.value(0)
    self.spi.write([cmd])
    self.dc.value(1)
    if value:
      self.spi.write(value)

  def send_data16(self, data):
    self.spi.write([data>>8, data&0xff])

  def send_buf(self,buf):
    self.spi.write(buf)
