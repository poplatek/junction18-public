from picamera import PiCamera
from time import sleep
from time import time
import math

camera = PiCamera()
camera.rotation = 180
today = int(math.floor(time()))

camera.start_preview(alpha=200)
sleep(3)
camera.capture('/home/pi/pics/test_' + str(today) + '.jpg')
camera.stop_preview()



