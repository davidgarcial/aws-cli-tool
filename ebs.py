import boto3
from ec2 import EC2

class EBS: 
    def __init__(self, user):
        self.user = user
        self.ebs = boto3.resource(
            "ec2",
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region_name = user.region_name
        )

        self.ebs_client = boto3.client(
            "ec2", 
            aws_access_key_id = user.accessKey,
            aws_secret_access_key= user.secretAccessKey,
            region_name = user.region_name
        )

    def getAllVolumes(self):
        print(f'EBS all volumes information:')
        volumes = self.ebs.volumes.all()
        for vol in volumes:
            print('\t \t |', vol.id)

    def attachVolume(self):
        self.getAllVolumes()
        print(f'Attach a volume to an instance')
        volume = input("Provide an volume id: ")

        if not volume:
            return

        EC2(self.user).list_instances()
        instance_id = input("Provide an instance id: ")

        if not instance_id:
            return

        try: 
            self.ebs_client.attach_volume(InstanceId=instance_id, VolumeId=volume, Device='/dev/sdf')
            print('Success Volume Attached')

        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')
        
    def detachVolume(self):
        self.getAllVolumes()
        print(f'Detach a volume from an instance')
        volume = input("Provide an volume id: ")

        if not volume:
            return
            
        EC2(self.user).list_instances()
        instance_id = input("Provide an instance id: ")

        if not instance_id:
            return
        
        try:
            self.ebs_client.detach_volume(InstanceId=instance_id, VolumeId=volume)
            print('Success Volume Dettach')
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')

    def listSnapshots(self):
        print(f'List all snapshots')
        res = self.ebs_client.describe_snapshots(OwnerIds=['self'])

        for snap in res['Snapshots']:
            print('\t |', snap['SnapshotId'])

    def takeSnapshot(self):
        print('Create a snapshot')

        self.getAllVolumes()
        volume = input("Provide an volume id: ")

        if not volume:
            return

        try:
            self.ebs.create_snapshot(VolumeId=volume)
            print(f'Snapshot created successfully')
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')

    def deleteSnapshot(self):
        print('Delete a snapshot')

        self.listSnapshots()
        snap = input("Provide an snapshot id: ")

        if not snap:
            return

        try:
            self.ebs_client.delete_snapshot(SnapshotId=snap)
            
            print(f'Snapshot deleted successfully')
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')

    def createVolumeFromSnapshot(self):
        print('Create Volume From Snapshot')

        self.listSnapshots()
        snap = input("Provide an snapshot id: ")

        if not snap:
            return

        try:
            self.ebs_client.create_volume(SnapshotId=snap, AvailabilityZone="us-east-2a")
            print(f'Volume from snapshot created successfully')
        except Exception as e:
            print(e)
            print(f'Something goes wrong try again')

