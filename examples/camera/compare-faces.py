import boto3

client = boto3.client('rekognition')
bucket = 'raspberry-camera'

response = client.compare_faces(
    SimilarityThreshold=90,
    SourceImage={
        'S3Object': {
            'Bucket': bucket,
            'Name': 'pic1.jpg',
        },
    },
    TargetImage={
        'S3Object': {
            'Bucket': bucket,
            'Name': 'pic2.jpg',
        },
    },
)

print(response)
