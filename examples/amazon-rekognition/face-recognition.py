# A simple example of how to use AWS Rekognition for face recognition for
# images from Raspberry Pi camera

import boto3
import picamera

# Name of the Collection of face data in Rekognition
COLLECTION='CollectionName'

client = boto3.client('rekognition')

def capture_image():
    """ Takes a picture with Raspberry Pi camera and rotates it by 180
        degrees. Returns the image as a binary blob. """
    camera_tmp = '/tmp/camera.png'
    with picamera.PiCamera() as camera:
        camera.rotation = 180
        camera.capture(camera_tmp)
    return file(camera_tmp).read()

def search_image(image_blob):
    """ Matches the largest detected face in the input image with the
        Collection, returns the match list from the AWS API as is, or empty
        list if there are no matches or no faces detected in the image """
    try:
        response = client.search_faces_by_image(
                CollectionId=COLLECTION,
                Image={"Bytes":image_blob}
            )
        return response['FaceMatches']
    except:
        # If no faces are detected in the image an exception is raised
        return []

if __name__ == '__main__':
    image_blob = capture_image()
    matches = search_image(image_blob)
    # matches will be a list of possible matches with different faces from the
    # collection, along with the confidence of the match
    print(matches)
