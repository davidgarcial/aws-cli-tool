import boto3

class EC2: 
    def __init__(self, user):
        self.ec2 = boto3.client(
            "ec2", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region_name = user.region_name
        )

        self.ec2_resource = boto3.resource(
            "ec2", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region_name = user.region_name
        )
    
    def printInstance(self, instanceInfo):
        print(f'\t EC2 instance "{instanceInfo["Tags"][0]["Value"]}" information:')
        print(f'\t \t | Instance state: {instanceInfo["State"]["Name"]}')
        print(f'\t \t | Instance ID: {instanceInfo["InstanceId"]}')
        print(f'\t \t | Instance AMI ID: {instanceInfo["ImageId"]}')
        print(f'\t \t | Instance Launch Time: {instanceInfo["LaunchTime"]}')
        print(f'\t \t | Instance Region: us-east-2')
        print('-'*60)

    def list_instances(self):
        instances = self.ec2.describe_instances()

        print(f'EC2 Running instances information:')
        print('-'*60)
        
        for instance in instances["Reservations"]:
            if instance["Instances"][0]["State"]["Name"] == "running":
                self.printInstance(instance["Instances"][0])
        
        print(f'EC2 NOT Running instances information:')

        print('-'*60)
        for instance in instances["Reservations"]:
            if not instance["Instances"][0]["State"]["Name"] == "running":
                self.printInstance(instance["Instances"][0])     
            
    def start_stop(self, action):
        instance_id = input("Provide an instance id: ")
        
        if action == 'ON':
            try:
                self.ec2.start_instances(InstanceIds=[instance_id])
                waiter = self.ec2.get_waiter('instance_running')
                waiter.wait(InstanceIds=[instance_id])
                print(f'EC2 ', instance_id, " was started")
            except Exception as e:
                print(e)
                print(f'Something goes wrong try again')
        else:
            try:
                self.ec2.stop_instances(InstanceIds=[instance_id])
                print(f'EC2 ', instance_id, " was stopped")
            except Exception as e:
                print(e)
                print(f'Something goes wrong try again')

    def createAmi(self):
        print(f'Create AMI from instance')
        self.list_instances()
        instance_id = input("Provide an instance id: ")
        name = input("Provide a name: ")

        try:
            self.ec2.create_image(InstanceId=instance_id, Name=name)
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')

        print(f'AMI created successfully')

    def deleteAmi(self):
        print(f'\t Delete AMI from instance')
        images = self.ec2.describe_images(Owners=['self'])
        
        for image in images['Images']:
            print('\t \t | ', image['ImageId'])

        image_id = input("Provide an ami id: ")

        if not image_id:
            return

        try:
            res = self.ec2.deregister_image(ImageId=image_id)
        
            if res['ResponseMetadata']['HTTPStatusCode'] == 200:
                print(f'AMI deleted successfully')
        
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')
            