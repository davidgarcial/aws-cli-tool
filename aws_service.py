import boto3

class AWSService: 
    def getEC2Resource(self, user):
        return boto3.resource(
            "ec2",
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region = user.region
        )

    def getEC2Client(self, user):
        return boto3.client(
            "ec2", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region = user.region
        )

    def getCloudWatchClient(self, user):
        return boto3.client(
            "cloudwatch", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region = user.region
        )

    def getS3Resource(self, user):
        return boto3.resource(
            "s3", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region = user.region
        )

    def getS3Client(self, user):
        return boto3.client(
            "s3", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region = user.region
        )