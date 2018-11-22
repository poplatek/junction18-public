import boto3

client = boto3.client('rekognition')
bucket = 'raspberry-camera'

response = client.detect_text(
    Image={
        'S3Object': {
            'Bucket': bucket,
            'Name': 'pic2.jpg'
        }
    }
)

print(response)
