import boto3

def getEC2Resource(user):
    resource = boto3.resource(
        "ec2",
        aws_access_key_id = user.accessKey,
        aws_secret_access_key= user.secretAccessKey,
        region_name = user.region
    )

    return resource

def getEC2Client(user):
    return boto3.client(
        "ec2", 
        aws_access_key_id = user.accessKey,
        aws_secret_access_key= user.secretAccessKey,
        region_name = user.region
    )

def getCloudWatchClient(user):
    return boto3.client(
        "cloudwatch", 
        aws_access_key_id = user.accessKey,
        aws_secret_access_key= user.secretAccessKey,
        region_name = user.region
    )

def getS3Resource(user):
    return boto3.resource(
        "s3", 
        aws_access_key_id = user.accessKey,
        aws_secret_access_key= user.secretAccessKey,
        region_name = user.region
    )

def getS3Client(user):
    return boto3.client(
        "s3", 
        aws_access_key_id = user.accessKey,
        aws_secret_access_key= user.secretAccessKey,
        region_name = user.region
    )