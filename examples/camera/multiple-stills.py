from picamera import PiCamera
from time import sleep
from time import time
import math

camera = PiCamera()
camera.rotation = 180

camera.start_preview(alpha=200)
for i in range(5):
    sleep(3)
    today = int(math.floor(time()))
    camera.capture('/home/pi/pics/test_' + str(today) + '.jpg')
    print('saved image: pics/' + str(today) + '.jpg')

camera.stop_preview()



