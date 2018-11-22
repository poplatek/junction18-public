from picamera import PiCamera
from time import sleep
from time import time
import boto3
import math
import base64

camera = PiCamera()
camera.rotation = 180
today = int(math.floor(time()))
client = boto3.client('rekognition')
bucket = 'raspberry-camera'

print('Taking picture...')
camera.start_preview(alpha=200)
sleep(3)
picpath = '/home/pi/pics/test_' + str(today) + '.jpg'
camera.capture(picpath)
camera.stop_preview()

with open(picpath, "rb") as imageFile:
  imageBytes = imageFile.read()
  print('Comparing images..')
  response = client.compare_faces(
    SimilarityThreshold=90,
    SourceImage={
      'Bytes':imageBytes
    },
    TargetImage={
      'S3Object': {
        'Bucket': bucket,
        'Name': 'pic2.jpg'
      }
    }
  )
  print('Done, results:')
  print(response)
