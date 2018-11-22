## Amazon Rekognition examples

Here are some simple examples of using Amazon Rekognition to compare images
or detect objects from images. For most Rekognition operations images can be
either in S3 or included as a binary in the API call.

# Face recognition

For face recognition there has to be a collection of face data, which is used
to recognize faces from the source image. Amazon does not save the images,
only the analyzed data required for the recognition.

Collection can be created with Python, the same way face recognition example passes the camera image for detection, but it can be done on command line as well, using awscli.

First upload the face images to S3. Then create the face collection:

    export COL=CollectionName
    aws rekognition create-collection --collection-id $COL
    aws rekognition index-faces --collection-id $COL \
        --image '{"S3Object":{"Bucket":"bucket","Name":"face1.jpg"}}' \
        --external-image-id custom-id1
    aws rekognition index-faces --collection-id $COL \
        --image '{"S3Object":{"Bucket":"bucket","Name":"face2.jpg"}}' \
        --external-image-id custom-id2

As a simple test you can try if Rekognition recognizes one of the source
images:

    aws rekognition search-faces-by-image --collection-id $COL \
        --image '{"S3Object":{"Bucket":"bucket","Name":"face2.jpg"}}'

Amazon's recommendations for the input images:
https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-facial-input-images.html

Full documentation for using Rekognition with Python and Boto 3 is available
at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html
