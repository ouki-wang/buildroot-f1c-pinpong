# -*- coding: utf-8 -*-
import os
import json
import freetype
from PIL import Image, ImageSequence

class FRAME_BUF(object):
  
  blend_mode = 0
  kerning    = 0
  rowledge   = 0

  part_flush = 0
  
  font_width    = 30
  font_height   = 30
  
  #颜色格式列表
  color_format_list = ['MVLSB','RGB565']

  enFontCode = {
    " ": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "!": [0,0,24,60,60,60,24,24,24,0,24,24,0,0,0,0],
    "\"": [0,99,99,99,34,0,0,0,0,0,0,0,0,0,0,0],
    "#": [0,0,0,54,54,127,54,54,54,127,54,54,0,0,0,0],
    "$": [12,12,62,99,97,96,62,3,3,67,99,62,12,12,0,0],
    "%": [0,0,0,0,0,97,99,6,12,24,51,99,0,0,0,0],
    "&": [0,0,0,28,54,54,28,59,110,102,102,59,0,0,0,0],
    "'": [0,48,48,48,96,0,0,0,0,0,0,0,0,0,0,0],
    "`": [24,24,12,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "(": [0,0,12,24,24,48,48,48,48,24,24,12,0,0,0,0],
    ")": [0,0,24,12,12,6,6,6,6,12,12,24,0,0,0,0],
    "*": [0,0,0,0,66,102,60,255,60,102,66,0,0,0,0,0],
    "+": [0,0,0,0,24,24,24,255,24,24,24,0,0,0,0,0],
    ",": [0,0,0,0,0,0,0,0,0,0,24,24,24,48,0,0],
    "-": [0,0,0,0,0,0,0,255,0,0,0,0,0,0,0,0],
    ".": [0,0,0,0,0,0,0,0,0,0,24,24,0,0,0,0],
    "/": [0,0,1,3,7,14,28,56,112,224,192,128,0,0,0,0],
    "0": [0,0,62,99,99,99,107,107,99,99,99,62,0,0,0,0],
    "1": [0,0,12,28,60,12,12,12,12,12,12,63,0,0,0,0],
    "2": [0,0,62,99,3,6,12,24,48,97,99,127,0,0,0,0],
    "3": [0,0,62,99,3,3,30,3,3,3,99,62,0,0,0,0],
    "4": [0,0,6,14,30,54,102,102,127,6,6,15,0,0,0,0],
    "5": [0,0,127,96,96,96,126,3,3,99,115,62,0,0,0,0],
    "6": [0,0,28,48,96,96,126,99,99,99,99,62,0,0,0,0],
    "7": [0,0,127,99,3,6,6,12,12,24,24,24,0,0,0,0],
    "8": [0,0,62,99,99,99,62,99,99,99,99,62,0,0,0,0],
    "9": [0,0,62,99,99,99,99,63,3,3,6,60,0,0,0,0],
    ":": [0,0,0,0,0,24,24,0,0,0,24,24,0,0,0,0],
    ";": [0,0,0,0,0,24,24,0,0,0,24,24,24,48,0,0],
    "<": [0,0,0,6,12,24,48,96,48,24,12,6,0,0,0,0],
    "=": [0,0,0,0,0,0,126,0,0,126,0,0,0,0,0,0],
    ">": [0,0,0,96,48,24,12,6,12,24,48,96,0,0,0,0],
    "?": [0,0,62,99,99,6,12,12,12,0,12,12,0,0,0,0],
    "@": [0,0,62,99,99,111,107,107,110,96,96,62,0,0,0,0],
    "A": [0,0,8,28,54,99,99,99,127,99,99,99,0,0,0,0],
    "B": [0,0,126,51,51,51,62,51,51,51,51,126,0,0,0,0],
    "C": [0,0,30,51,97,96,96,96,96,97,51,30,0,0,0,0],
    "D": [0,0,124,54,51,51,51,51,51,51,54,124,0,0,0,0],
    "E": [0,0,127,51,49,52,60,52,48,49,51,127,0,0,0,0],
    "F": [0,0,127,51,49,52,60,52,48,48,48,120,0,0,0,0],
    "G": [0,0,30,51,97,96,96,111,99,99,55,29,0,0,0,0],
    "H": [0,0,99,99,99,99,127,99,99,99,99,99,0,0,0,0],
    "I": [0,0,60,24,24,24,24,24,24,24,24,60,0,0,0,0],
    "J": [0,0,15,6,6,6,6,6,6,102,102,60,0,0,0,0],
    "K": [0,0,115,51,54,54,60,54,54,51,51,115,0,0,0,0],
    "L": [0,0,120,48,48,48,48,48,48,49,51,127,0,0,0,0],
    "M": [0,0,99,119,127,107,99,99,99,99,99,99,0,0,0,0],
    "N": [0,0,99,99,115,123,127,111,103,99,99,99,0,0,0,0],
    "O": [0,0,28,54,99,99,99,99,99,99,54,28,0,0,0,0],
    "P": [0,0,126,51,51,51,62,48,48,48,48,120,0,0,0,0],
    "Q": [0,0,62,99,99,99,99,99,99,107,111,62,6,7,0,0],
    "R": [0,0,126,51,51,51,62,54,54,51,51,115,0,0,0,0],
    "S": [0,0,62,99,99,48,28,6,3,99,99,62,0,0,0,0],
    "T": [0,0,255,219,153,24,24,24,24,24,24,60,0,0,0,0],
    "U": [0,0,99,99,99,99,99,99,99,99,99,62,0,0,0,0],
    "V": [0,0,99,99,99,99,99,99,99,54,28,8,0,0,0,0],
    "W": [0,0,99,99,99,99,99,107,107,127,54,54,0,0,0,0],
    "X": [0,0,195,195,102,60,24,24,60,102,195,195,0,0,0,0],
    "Y": [0,0,195,195,195,102,60,24,24,24,24,60,0,0,0,0],
    "Z": [0,0,127,99,67,6,12,24,48,97,99,127,0,0,0,0],
    "[": [0,0,60,48,48,48,48,48,48,48,48,60,0,0,0,0],
    "\\": [0,0,128,192,224,112,56,28,14,7,3,1,0,0,0,0],
    "]": [0,0,60,12,12,12,12,12,12,12,12,60,0,0,0,0],
    "^": [8,28,54,99,0,0,0,0,0,0,0,0,0,0,0,0],
    "_": [0,0,0,0,0,0,0,0,0,0,0,0,255,0,0,0],
    "a": [0,0,0,0,0,60,70,6,62,102,102,59,0,0,0,0],
    "b": [0,0,112,48,48,60,54,51,51,51,51,110,0,0,0,0],
    "c": [0,0,0,0,0,62,99,96,96,96,99,62,0,0,0,0],
    "d": [0,0,14,6,6,30,54,102,102,102,102,59,0,0,0,0],
    "e": [0,0,0,0,0,62,99,99,126,96,99,62,0,0,0,0],
    "f": [0,0,28,54,50,48,124,48,48,48,48,120,0,0,0,0],
    "g": [0,0,0,0,0,59,102,102,102,102,62,6,102,60,0,0],
    "h": [0,0,112,48,48,54,59,51,51,51,51,115,0,0,0,0],
    "i": [0,0,12,12,0,28,12,12,12,12,12,30,0,0,0,0],
    "j": [0,0,6,6,0,14,6,6,6,6,6,102,102,60,0,0],
    "k": [0,0,112,48,48,51,51,54,60,54,51,115,0,0,0,0],
    "l": [0,0,28,12,12,12,12,12,12,12,12,30,0,0,0,0],
    "m": [0,0,0,0,0,110,127,107,107,107,107,107,0,0,0,0],
    "n": [0,0,0,0,0,110,51,51,51,51,51,51,0,0,0,0],
    "o": [0,0,0,0,0,62,99,99,99,99,99,62,0,0,0,0],
    "p": [0,0,0,0,0,110,51,51,51,51,62,48,48,120,0,0],
    "q": [0,0,0,0,0,59,102,102,102,102,62,6,6,15,0,0],
    "r": [0,0,0,0,0,110,59,51,48,48,48,120,0,0,0,0],
    "s": [0,0,0,0,0,62,99,56,14,3,99,62,0,0,0,0],
    "t": [0,0,8,24,24,126,24,24,24,24,27,14,0,0,0,0],
    "u": [0,0,0,0,0,102,102,102,102,102,102,59,0,0,0,0],
    "v": [0,0,0,0,0,99,99,54,54,28,28,8,0,0,0,0],
    "w": [0,0,0,0,0,99,99,99,107,107,127,54,0,0,0,0],
    "x": [0,0,0,0,0,99,54,28,28,28,54,99,0,0,0,0],
    "y": [0,0,0,0,0,99,99,99,99,99,63,3,6,60,0,0],
    "z": [0,0,0,0,0,127,102,12,24,48,99,127,0,0,0,0],
    "{": [0,0,14,24,24,24,112,24,24,24,24,14,0,0,0,0],
    "|": [0,0,24,24,24,24,24,0,24,24,24,24,24,0,0,0],
    "}": [0,0,112,24,24,24,14,24,24,24,24,112,0,0,0,0],
    "~": [0,0,59,110,0,0,0,0,0,0,0,0,0,0,0,]
    }
  
  bitmap_width  = 0
  bitmap_height = 0
  
  def __init__(self, buffer, width, height, format):
    self.width  = width
    self.height = height
    if format in self.color_format_list:
      self.format = format
    self.pixel = buffer
    self.ch_text_json = None

  def text(self, text, x, y, color, word_wrap, obj):
    if(self.format == self.color_format_list[1])|('font' in dir(self)):
      y = y + self.font_height
      char_index  = 0
      prev_char   = 0
      pen         = freetype.Vector()
      pen.x       = x  
      pen.y       = y 
      bottom_list = []
      cur_pen = freetype.Vector()
      for cur_char in text:
        glyph_index = self._face.get_char_index(cur_char)
        if (prev_char != 0)&(glyph_index != 0):
          if(self.kerning ==0):
            kerning = self._face.get_kerning(prev_char, cur_char)
            pen.x += kerning.x >> 6
          else:
            pen.x += self.kerning
        self._face.load_glyph(glyph_index)
        glyph = self._face.glyph
        bitmap = glyph.bitmap
        cur_pen.x = pen.x + glyph.bitmap_left
        cur_pen.y = pen.y - glyph.bitmap_top
        bitmap_bottom = bitmap.rows-glyph.bitmap_top
        bottom_list.append(bitmap_bottom)
        cols = cur_pen.x
        rows = cur_pen.y
        if( rows+bitmap.rows <= obj.height):
          if(cols+(bitmap.width) <= obj.width):
            cols += bitmap.width
            self.bitmap(bitmap, color, cur_pen.x, cur_pen.y, obj)
            pen.x += glyph.advance.x >> 6
            prev_char = cur_char
            char_index += 1
          else:
            if word_wrap:
              next_line_text = text[char_index:]
              if(self.rowledge == 0):
                self.text(next_line_text,0,y+max(bottom_list),color,word_wrap,obj)
              else:
                self.text(next_line_text,0,y+self.rowledge,color,word_wrap,obj)
              break
            else:
              break
      if(cols >= obj.width): cols = obj.width -1
      if(self.part_flush!=0):
        self.flush(obj,x,y-self.font_height,cols,y+max(bottom_list))
    elif(self.format == self.color_format_list[0]):
      pos_x = x
      if not isinstance(text, str):
          return
      for i in text:
          if ord(i) < 128:
              count = 0
              str_buf = self.enFontCode[i]
              for b in str_buf:
                  self.set_ascii(x, y+count, b, color,obj)
                  count += 1
              x += 8
          else:
              count = 0
              self.ch_text_json = json.load(open("Lib/fonts_msyh.ttf.json", 'r', encoding='utf-8'))
              if not self.ch_text_json['data'].get(i):
                  i = " "
              str_buf = self.ch_text_json['data'].get(i)
              for b in str_buf:
                  if count % 2:
                      self.set_ascii(x + 8, y + count - 1, b, color, obj)
                  else:
                      self.set_ascii(x, y + count, b, color, obj)
                  count += 1
              x += 16
      if(self.part_flush!=0):
        self.flush(obj,pos_x,y,pos_x+len(text)*8,y+8)

  def hline(self, x, y, width, color):
      self._fill_rect(x, y, width, 1, color)
  
  def vline(self, x, y, height, color):
      self._fill_rect(x, y, 1, height, color)

  def set_ascii(self, x, y, b, color, obj):
    if not color:
        b = 255 - b
    b = bin(b)[2:].rjust(8, '0')
    count = 0
    for i in b:
        i = int(i)
        self._set_pixel(x+count, y, i, obj)
        count += 1
  
  def bitmap(self, bitmap, color, x, y, obj):
    cols = bitmap.width
    rows = bitmap.rows
    glyph_pixels = bitmap.buffer
    temp = x
    for row in range(rows):
      for col in range(cols):
        if glyph_pixels[row * cols + col] != 0:
          self._set_pixel(x, y, color, obj)
          x = x + 1
        else:    
          x = x + 1 #该像素点没数据，跳过
      y = y + 1     #换行
      x = temp      #x轴方向的起始坐标
  
  def line(self,x1,y1,x2,y2,color,obj):
    dx = x2 - x1
    dy = y2 - y1
    if dx > 0:incx = 1
    elif dx == 0:incx = 0 
    else:
      incx = -1
      dx = -dx
    if dy > 0:incy = 1
    elif dy == 0:incy = 0
    else:
      incy = -1
      dy = -dy
    if dx > dy:distance = dx
    else:distance = dy
    x = x1
    y = y1
    x_temp = 0
    y_temp = 0
    for i in range(0,distance):
      self._set_pixel(x,y,color,obj)
      x_temp += dx
      if x_temp > distance:
        x_temp -= distance
        x += incx
      y_temp += dy
      if y_temp > distance:
        y_temp -= distance
        y += incy
    if self.part_flush:
      self.flush(obj,x1,y1,x2+1,y2+1)    
  
  def rect(self,x,y,w,h,color,obj):
    self._fill_rect(x,y,w,1,color,obj)
    self._fill_rect(x+w-1,y,1,h,color,obj)
    self._fill_rect(x,y+h,w,1,color,obj)
    self._fill_rect(x,y,1,h,color,obj)
    if self.part_flush:
      self.flush(obj,x,y,x+w,y+h)
  
  def fill_rect(self,x,y,w,h,color,obj):
    if(x<obj.width)&(y<obj.height):
      if((x+w)>obj.width): 
       w = obj.width - x
      if((y+h)>obj.height):
       h = obj.height - y
    for heigth in range(y,y+h):
      for width in range(x,x+w):
        self._set_pixel(width,heigth,color,obj)
    if self.part_flush:
      self.flush(obj,x,y,x+w,y+h)
  
  def circle(self, x, y, r, color, obj):#画圆
    r = abs(r)
    if r == 1:
      r = 2
    x_axis = 0
    y_axis = r
    var = 3 - (r << 1)
    while (x_axis <= y_axis):
      #填充像素点信息
      self._set_pixel(x + x_axis, y + y_axis, color, obj)
      self._set_pixel(x - x_axis, y + y_axis, color, obj)
      self._set_pixel(x + x_axis, y - y_axis, color, obj)
      self._set_pixel(x - x_axis, y - y_axis, color, obj)
      self._set_pixel(x + y_axis, y + x_axis, color, obj)
      self._set_pixel(x - y_axis, y + x_axis, color, obj)
      self._set_pixel(x + y_axis, y - x_axis, color, obj)
      self._set_pixel(x - y_axis, y - x_axis, color, obj)
      if var < 0:
        var += 4 * x_axis + 6
      else:
        var += 10 + 4 * (x_axis - y_axis)
        y_axis -= 1
      x_axis += 1
    if self.part_flush:
      if(0<x-r<obj.width)&(0<y-r<obj.height)&(0<x+r<obj.width)&(0<y+r<obj.height):
        self.flush(obj,x-r,y-r,x+r+1,y+r+1)
      elif(x==0&y==0):
        self.flush(obj,x-r,y-r,x+r+1,y+r+1)
      else:
        self.flush(obj,x-r,y-r,x+r+1,y+r+1,True)
  
  def fill_circle(self,x,y,r,color,obj):#画圆
    r = abs(r)
    if r == 1:
      r = 2
    x_axis =  0
    y_axis = r
    var = 3 - (r << 1)
    while (x_axis <= y_axis):
      #填充像素点信息
      self._fill_rect(x + x_axis, y - y_axis, 1, 2 * y_axis + 1, color, obj)
      self._fill_rect(x + y_axis, y - x_axis, 1, 2 * x_axis + 1, color, obj)
      self._fill_rect(x - x_axis, y - y_axis, 1, 2 * y_axis + 1, color, obj)
      self._fill_rect(x - y_axis, y - x_axis, 1, 2 * x_axis + 1, color, obj)
      if var < 0:
        var += 4 * x_axis + 6
      else:
        var += 10 + 4 * (x_axis - y_axis)
        y_axis -= 1
      x_axis += 1
    if self.part_flush:
      if(0<x-r<obj.width)&(0<y-r<obj.height)&(0<x+r<obj.width)&(0<y+r<obj.height):
        self.flush(obj,x-r,y-r,x+r+1,y+r+1)
      elif(x==0&y==0):
        self.flush(obj,x-r,y-r,x+r+1,y+r+1)
      else:
        self.flush(obj,x-r,y-r,x+r+1,y+r+1,True)
  
  def picture(self,filename,x,y,size,obj):
    img = Image.open(filename)
    if((filename[-3:]) == "gif" or (filename[-3:]) == "GIF"):
      for frame in ImageSequence.all_frames(img):
        frame = frame.convert("RGB")
        frame.thumbnail((size,size))
        for i in range(0,frame.size[1]):
          for m in range(0,frame.size[0]):
            R = frame.getpixel((m,i))[0] >> 3
            G = frame.getpixel((m,i))[1] >> 2
            B = frame.getpixel((m,i))[2] >> 3
            color = (R << 11)|(G << 5)|(B)
            self.pixel[(y+i)*obj.width+(x+m)] = [color>>8,color]
        self.flush(obj,x,y,(x+size),(y+size))
    else:
      img = img.convert("RGB")
      img.thumbnail((size,size))
      for i in range(0,img.size[1]):
          for m in range(0,img.size[0]):
            R = img.getpixel((m,i))[0] >> 3
            G = img.getpixel((m,i))[1] >> 2
            B = img.getpixel((m,i))[2] >> 3
            color = (R << 11)|(G << 5)|(B)
            self.pixel[(y+i)*obj.width+(x+m)] = [color>>8,color]
      self.flush(obj,x,y,(x+size),(y+size))
  
  def fill(self,color,obj):
    self.fill_rect(0,0,self.width,self.height,color,obj)
  
  def set_blend_mode(self,mode):
    self.blend_mode = mode
  
  def set_flush_mode(self,mode):
    self.part_flush = mode
  
  def set_font(self,font,width,height,kerning,rowledge):
    self.font        = font
    self.font_width  = width
    self.font_height = height
    self.kerning     = kerning
    self.rowledge    = rowledge
    cwdpath,_  = os.path.split(os.path.realpath(__file__))
    self._face = freetype.Face(cwdpath+"/../base/"+self.font+".ttf")
    #直接指定字体像素大小
    self._face.set_pixel_sizes(self.font_width, self.font_height)
  
  def _fill_rect(self,x,y,w,h,color,obj):
    if(y<0)&(h == 1): return
    if(x<0)&(w == 1): return
    if(x<obj.width)&(y<obj.height):
      if(x<0)&(x+w>0):
        w = w + x
        x = 0
      if(y<0)&(y+h>0):
        h = h + y
        y = 0
      if((x+w)>obj.width)&(x>0): w = obj.width - x
      if((y+h)>obj.height)&(y>0):h = obj.height - y
      if(self.format == 'RGB565'):
        for height in range(y,y+h):
          for width in range(x,x+w):
            self._set_pixel(width,height,color,obj)
      elif(self.format == 'MVLSB'):
        for height in range(y, y+h):
          index = (height >> 3)* obj.width + x
          offset = height & 0x07
          for width in range(x,x+w):
            self.pixel[index] = (self.pixel[index] & ~(1 << offset)) | ((color != 0) << offset)
            index += 1
  
  def _set_pixel(self,x,y,color,obj):
    if((0<=y<obj.height)&(0<=x<=obj.width)):
      if(self.format == self.color_format_list[1]):
        if(self.blend_mode == 0):
            self.pixel[y*obj.width+x]   = [(color|self.pixel[y*obj.width+x][1])>>8,color|self.pixel[y*obj.width+x][1]]#这是二维列表
        else:
            self.pixel[y*obj.width+x]   = [color>>8,color]#这是二维列表
      elif(self.format == self.color_format_list[0]):
        index = (y>>3)*obj.width+x
        offset = y & 0x07
        self.pixel[index] = (self.pixel[index] & ~(1 << offset)) | ((color != 0) << offset)
  
  #flag 越界标识 False未越界
  def flush(self,obj,x1,y1,x2,y2,flag=False):
    x1 = 0 if(x1 <= 0) else x1
    x2 = 0 if(x2 <= 0) else x2
    y1 = 0 if(y1 <= 0) else y1
    y2 = 0 if(y2 <= 0) else y2 
    x1 = obj.width  if(x1 > obj.width)  else x1
    x2 = obj.width  if(x2 > obj.width)  else x2
    y1 = obj.height if(y1 > obj.height) else y1
    y2 = obj.height if(y1 > obj.height) else y2
    buf=[]
    if(self.format == self.color_format_list[1]):
      if flag == False:
        length_x =  abs(x1-x2) + 1
        length_y =  abs(y1-y2) + 1
      else:
        length_x =  abs(x1-x2)
        length_y =  abs(y1-y2)
      for y in range(0,length_y):
        buf += [n for a in self.pixel[((y1+y)*obj.width+x1):((y1+y)*obj.width+x1+length_x)] for n in a ]#展开成一维列表
      obj.flush(buf,x1,y1,x2,y2)
    elif(self.format == self.color_format_list[0]):
      y1 = (y1//8 - 1) if(y1%8 != 0) else (y1//8)
      y1 = 0 if(y1<0) else y1
      y2 = (y2//8 + 1) if(y2%8 != 0) else (y2//8)
      y2 = 0 if(y2<0) else y2
      y2 = (obj.height//8)-1 if(y2 >=(obj.height//8)) else y2
      x2 = obj.width -1 if(x2 >= obj.width) else x2 - 1
      length_x  =  abs(x1-x2) 
      length_y  =  abs(y1-y2) + 1
      for y in range(0,length_y):
        buf += self.pixel[((y1+y)*obj.width+x1):((y1+y)*obj.width+x1+length_x+1)]
      obj.flush(buf,x1,y1,x2,y2)