from picamera import PiCamera
from time import sleep
from time import time
import math

camera = PiCamera()
today = int(math.floor(time()))

camera.start_preview()
camera.start_recording('/home/pi/videos/video_' + str(today) + '.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
