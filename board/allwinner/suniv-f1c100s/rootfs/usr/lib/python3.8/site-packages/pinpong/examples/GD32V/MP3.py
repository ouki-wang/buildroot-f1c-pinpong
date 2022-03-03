import time
from pinpong.board import Board
from pinpong.libs.dfrobot_mp3 import MP3

Board("GD32V").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
#Board("GD32V","COM36").begin()   #windows下指定端口初始化
#Board("GD32V","/dev/ttyACM0").begin()   #linux下指定端口初始化
#Board("GD32V","/dev/cu.usbmodem14101").begin()   #mac下指定端口初始化

mp3 = MP3()

mp3.playList(1)      #播放第几首歌曲
#mp3.pause()          #暂停播放
#mp3.play()           #播放
#mp3.next()           #播放下一首歌曲
#mp3.prev()           #播放上一首歌曲
#mp3.end()            #结束播放
#mp3.volume_up()      #音量加1
#mp3.volume_down()    #音量减1
#mp3.volume()    #音量设置
#time.sleep(6)
#mp3.query_play_status()    #查询播放状态

