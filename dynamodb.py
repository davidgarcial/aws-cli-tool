# AAmazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability
# DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, 
# so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.
# In simple words its a reliable, small and serverless db that allows alocate any kind of information without a previous model 
# Their most commun scenarios are:
#   - Applications with large amounts of data and strict latency requirements.
#   - Serverless applications using AWS Lambda.
#   - Data sets with simple, known access patterns.

import time
import boto3
from botocore.exceptions import ClientError

class AmazonDB():
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id = "AKIA3PT2Q4JWTKP6KFNH",
            aws_secret_access_key= "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",
            region_name = "us-east-2"
        )

    def getTable(self, tableName):
        return self.dynamodb.Table(tableName)

    def getItem(self, table, id, name):
        try:
            response = table.get_item(
                Key={'id': id, 'name': name}
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def createTable(self, tableName):
        try:
            table = self.dynamodb.create_table(
                TableName=tableName,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'name',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    # ReadCapacityUnits set to 10 strongly consistent reads per second
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
                }
            )
            return table
        except ClientError as er:
            if er.response['Error']['Message']:
                print(er.response['Error']['Message'])

    def loadData(self, tableName, id, name):
        response = self.getTable(tableName).put_item(
            Item={
                'id': id,
                'name': name
            }
        )
        return response

    def deleteData(self, tableName, id, name):
        try:
            response = self.getTable(tableName).delete_item(
                Key={
                    'id': id,
                    'name': name
                }
                # Conditional request
                #ConditionExpression="info.info_timestamp <= :value",
                #ExpressionAttributeValues={
                #    ":value": info_timestamp
                #}
            )
        except ClientError as er:
            if er.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(er.response['Error']['Message'])
            else:
                raise
        
        return response

    def deleteTable(self, tableName):
        table = self.getTable(tableName)
        table.delete()

    def main(self):
        self.createTable("testTable")

        table = self.getTable("testTable")
        
        print(self.loadData("testTable", "1", "testSampleData"))
        print(self.getItem(table, "1", "testSampleData"))

        print("The program will wait 10 sec, you can check the table and data in aws")
        time.sleep(10)

        print("The data and table will be deleted")

        print(self.deleteData("testTable", "1", "testSampleData"))
        print(self.deleteTable("testTable"))

AmazonDB().main()