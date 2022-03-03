# -*- coding: utf-8 -*-

import time
from pinpong.extension.globalvar import *
from pinpong.board import Pin

class GD32Sensor_buttonA:
  def __init__(self, board=None):
    self.first_flag = True
  
  def is_pressed(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_buttonA_is_pressed()
  
  def irq(self, trigger=None, handler=None):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    self.Pin = Pin(Pin.P27)
    self.board.board.GD32V_buttonA_irq(trigger, handler, self.Pin)
  
  def value(self):
    return 1 if self.is_pressed() else 0

class GD32Sensor_buttonB:
  def __init__(self, board=None):
    self.first_flag = True
  
  def is_pressed(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_buttonB_is_pressed()
  
  def irq(self, trigger=None, handler=None):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    self.Pin = Pin(Pin.P28)
    return self.board.board.GD32V_buttonB_irq(trigger, handler, self.Pin)
	
  def value(self):
    return 1 if self.is_pressed() else 0

class GD32Sensor_light:
  def __init__(self, board=None):
    self.first_flag = True
  
  def read(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_read_light()

class GD32Sensor_acc:
  def __init__(self, board=None):
    self.first_flag = True
  
  def get_x(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_accelerometer_X()
  
  def get_y(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_accelerometer_Y()
  
  def get_z(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_accelerometer_Z()

class GD32Sensor_gyro:
  def __init__(self, board=None):
    self.first_flag = True
  
  def get_x(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_Macceleration_X()
  
  def get_y(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_Macceleration_Y()
  
  def get_z(self):
    if self.first_flag:
      self.first_flag = False
      self.board = get_globalvar_value("GD32V")
      self.board.board._report_sensor()
    return self.board.board.GD32V_get_Macceleration_Z()


button_a = GD32Sensor_buttonA()  #兼容micropython方法
button_b = GD32Sensor_buttonB()
light = GD32Sensor_light()
accelerometer = GD32Sensor_acc()
gyroscope = GD32Sensor_gyro()