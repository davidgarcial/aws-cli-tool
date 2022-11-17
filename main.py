from login import Login
from ec2 import EC2
from s3 import S3
from ebs import EBS
from monitor import Monitor
from clear import clear

class Main:
    def __init__(self):
        self.Login = Login()
        self.user = self.Login.login_check()

        if self.user:
            print("Login successful!!")
            clear(2)
            self.ec2 = EC2(self.user)
            self.ebs = EBS(self.user)
            self.s3 = S3(self.user)
            self.monitor = Monitor(self.user)
            self.generalMenu()

    def generalMenu(self):
        print("AWS Manager")
        print('\t 1.-EC2 Instances')
        print('\t 2.-EBS Storage')
        print('\t 3.-Monitoring')

        if self.isAdmin():
            print('\t 4.-S3 Storage')

        print('\t 5.-Exit')

        menuOption = int(input("Select an option: "))

        match menuOption:
            case 1:
                clear(2)
                self.ec2Menu()
            case 2:
                clear(2)
                self.ebsMenu()
            case 4:
                if not self.isAdmin():
                    clear(0)
                    self.generalMenu()
                clear(2)
                self.s3Menu()
            case 3:
                clear(2)
                self.monitorMenu()
            case 5:
                quit()
            case _:
                clear(0)
                self.generalMenu()

    def ec2Menu(self):
        print('EC2 Instances')
        print('\t 1.-List all instances')
        print('\t 2.-Start instance (by ID)')
        print('\t 3.-Stop instance (by ID)')
        print('\t 4.-Create AMI from instance')
        
        if self.isAdmin():
            print('\t 5.-Delete AMI (Admin Only)')
        
        print('\t 6.-Return')
        print('\t 7.-Exit')

        option = int(input("Select an options: "))

        match option:
            case 1:
                self.ec2.list_instances()
                clear(2)
                self.ec2Menu()
            case 2:
                self.ec2.list_instances()
                self.ec2.start_stop("ON")
            case 3:
                self.ec2.list_instances()
                self.ec2.start_stop("OFF")
            case 4:
                self.ec2.createAmi()
            case 5:
                if not self.isAdmin():
                    clear(0)
                    self.ec2Menu()

                self.ec2.deleteAmi()
            case 6:
                self.generalMenu()
                clear(0)
                return
            case 7:
                quit()
            case _:
                clear(0)
                self.ec2Menu()

        clear(2)
        self.ec2Menu()

    def ebsMenu(self):
        print('EBS Storage')
        print('\t 1.-List all volumes')
        print('\t 2.-Attach an existing volume to an instance')
        print('\t 3.-Detach a volume from an instance')
        print('\t 4.-List all snapshots')

        if self.isAdmin():
            print('\t 5.-Take a snapshot of a specific volume (specified by the user) (Admin Only)')
            print('\t 6.-Delete a snapshot (Admin Only)')
            print('\t 7.-Create a volume from a snapshot (Admin Only)')

        print('\t 8.-Return')
        print('\t 9.-Exit')

        option = int(input("Select an options: "))

        match option:
            case 1:
                self.ebs.getAllVolumes()
                clear(2)
                self.ebsMenu()
            case 2:
                self.ebs.attachVolume()
            case 3:
                self.ebs.detachVolume()
            case 4:
                self.ebs.listSnapshots()
            case 5:
                if not self.isAdmin():
                    clear(0)
                    self.ebsMenu()
                self.ebs.takeSnapshot()
            case 6:
                if not self.isAdmin():
                    clear(0)
                    self.ebsMenu()
                self.ebs.deleteSnapshot()
            case 7:
                if not self.isAdmin():
                    clear(0)
                    self.ebsMenu()
                self.ebs.createVolumeFromSnapshot()
            case 8:
                self.generalMenu()
                clear(0)
                return
            case 9:
                quit()
            case _:
                clear(0)
                self.ebsMenu()

        clear(2)
        self.ebsMenu()

    def s3Menu(self):
        print('S3 Storage')
        print('\t 1.-List all objects in a bucket (Admin Only)')
        print('\t 2.-Upload an object (Admin Only)')
        print('\t 3.-Download an object (make it easy to select from the existing objects) (Admin Only)')
        print('\t 4.-Delete an object (Admin Only')
        print('\t 5.-Delete a bucket (Admin Only)')
        print('\t 6.-Return')
        print('\t 7.-Exit')

        option = int(input("Select an options: "))

        match option:
            case 1:
                self.s3.bucketDetails()
                clear(2)
                self.s3Menu()
            case 2:
                self.s3.upload_file()
            case 3:
                self.s3.download_file()
            case 4:
                self.s3.delete_file()
            case 5:
                self.s3.delete_bucket()
            case 6:
                self.generalMenu()
                clear(0)
                return
            case 7:
                quit()
            case _:
                clear(0)
                self.s3Menu()

        clear(2)
        self.s3Menu()

    def monitorMenu(self):
        print('Monitoring')
        print('\t 1.-Display the CPU Utilization and CPU Credits Usage performance')
        print('\t 2.-Set an alarm')
        print('\t 3.-Return')
        print('\t 4.-Exit')

        option = int(input("Select an options: "))

        match option:
            case 1:
                self.monitor.cpuData()
                clear(2)
                self.monitorMenu()
            case 2:
                self.monitor.setAlarm()
                clear(2)
                self.monitorMenu()
            case 3:
                self.generalMenu()
                clear(0)
                return
            case 4:
                quit()
            case _:
                clear(0)
                self.monitorMenu()

        clear(2)
        self.monitorMenu()

    def isAdmin(self):
        if self.user.userType == "admin":
            return True
        
        return False

Main()