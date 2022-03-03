import time
import sys
from pinpong.board import gboard

_temperature      = 25.0
_acidVoltage      = 1640.44
_neutralVoltage   = 1220.0
class DFRobot_PH():
  def __init__(self, board=None, adc=None):
    if isinstance(board, int):
      board = gboard
    elif board is None:
      board = gboard
    self.adc = adc

  def begin(self):
    global _acidVoltage
    global _neutralVoltage
    try:
      with open('phdata.txt','r') as f:
        neutralVoltageLine = f.readline()
        neutralVoltageLine = neutralVoltageLine.strip('neutralVoltage=')
        _neutralVoltage    = float(neutralVoltageLine)
        acidVoltageLine    = f.readline()
        acidVoltageLine    = acidVoltageLine.strip('acidVoltage=')
        _acidVoltage       = float(acidVoltageLine)
    except :
      f=open('phdata.txt','w')
      #flist=f.readlines()
      flist   ='neutralVoltage='+ str(_neutralVoltage) + '\n'
      flist  +='acidVoltage='+ str(_acidVoltage) + '\n'
      #f=open('data.txt','w+')
      f.writelines(flist)
      f.close()
      print(">>>Reset to default parameters<<<")
  def readPH(self,temperature):
    global _acidVoltage
    global _neutralVoltage
    voltage = self.adc.read()*4
    print("voltage=",voltage)
    #slope     = (7.0-4.0)/((_neutralVoltage-1500.0)/3.0 - (_acidVoltage-1500.0)/3.0)
    k = (_neutralVoltage - _acidVoltage)/(7.0-4.0)
    b = _neutralVoltage - 7*k
    #print("_neutralVoltage - _acidVoltage=%f - %f"%(_neutralVoltage , _acidVoltage))
    #print("k=",k)
    #print("b=",b)
    #print("intercept=",intercept)
    #_phValue  = slope*(voltage-1500.0)/3.0+intercept
    _phValue  = (voltage-b)/k
    print("_phValue=",_phValue)
    return round(_phValue,2)
    #print("round _phValue=",_phValue)
    #return _phValue
  def calibration(self,ph,voltage=None):
    if ph == 7:
      v=0
      if voltage == None:
        for i in range(20):
          v = v + self.adc.read()*4
      voltage = v/20
      print("voltage=",voltage)
      print(">>>Buffer Solution:7.0")
      f=open('phdata.txt','r+')
      flist=f.readlines()
      flist[0]='neutralVoltage='+ str(voltage) + '\n'
      f=open('phdata.txt','w+')
      f.writelines(flist)
      f.close()
      print(">>>PH:7.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
    elif ph == 4:
      v=0
      if voltage == None:
        for i in range(20):
          v = v + self.adc.read()*4
      voltage = v/20
      print("voltage=",voltage)
      print(">>>Buffer Solution:4.0")
      f=open('phdata.txt','r+')
      flist=f.readlines()
      flist[1]='acidVoltage='+ str(voltage) + '\n'
      f=open('phdata.txt','w+')
      f.writelines(flist)
      f.close()
      print(">>>PH:4.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
    else:
      print(">>>Buffer Solution Error Try Again<<<")
