from ec2 import EC2
from aws_service import getEC2Client, getEC2Resource
from utils import handleError

class EBS: 
    def __init__(self, user):
        self.user = user
        self.ebs = getEC2Resource(user)
        self.ebs_client = getEC2Client(user)

    def getAllVolumes(self):
        print(f'EBS all volumes information:')
        volumes = self.ebs.volumes.all()

        for vol in volumes:
            print('\t \t |', vol.id)

        print('-'*60)

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

        except Exception as error:
            handleError(error)
        
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
        except Exception as error:
            handleError(error)

    def listSnapshots(self):
        print(f'List all snapshots')
        res = self.ebs_client.describe_snapshots(OwnerIds=['self'])

        for snap in res['Snapshots']:
            print('\t |', snap['SnapshotId'])
        
        print('-'*60)

    def takeSnapshot(self):
        print('Create a snapshot')

        self.getAllVolumes()
        volume = input("Provide an volume id: ")

        if not volume:
            return

        try:
            self.ebs.create_snapshot(VolumeId=volume)
            print(f'Snapshot created successfully')
        except Exception as error:
            handleError(error)

    def deleteSnapshot(self):
        print('Delete a snapshot')

        self.listSnapshots()
        snap = input("Provide an snapshot id: ")

        if not snap:
            return

        try:
            self.ebs_client.delete_snapshot(SnapshotId=snap)
            
            print(f'Snapshot deleted successfully')
        except Exception as error:
            handleError(error)

    def createVolumeFromSnapshot(self):
        print('Create Volume From Snapshot')

        self.listSnapshots()
        snap = input("Provide an snapshot id: ")

        if not snap:
            return

        try:
            self.ebs_client.create_volume(SnapshotId=snap, AvailabilityZone="us-east-2a")
            print(f'Volume from snapshot created successfully')
        except Exception as error:
            handleError(error)

