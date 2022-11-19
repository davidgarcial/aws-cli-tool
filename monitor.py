from datetime import datetime, timedelta
from ec2 import EC2
from aws_service import AWSService
from utils import handleError

class Monitor: 
    def __init__(self, user):
        aws_Service = AWSService()
        self.user = user
        self.cloudwatch = aws_Service.getCloudWatchClient(user)

    def cpuData(self):
        print(f'EC2 CPU (last 30 min) information')

        EC2(self.user).list_instances()
        instance_id = input("Provide an instance id: ")

        if not instance_id:
            return

        try:
            CPUCreditUsage = self.cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                StartTime= datetime.utcnow() - timedelta(seconds=1500),
                EndTime= datetime.utcnow(),
                Statistics=[
                    'Average',
                ],
                Unit='Percent',
                Period=86460,
                Dimensions=[
                    {
                    'Name': 'InstanceId',
                    'Value': instance_id
                    },
                ]
            )

            CPUUtilization = self.cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                StartTime= datetime.utcnow() - timedelta(seconds=1500),
                EndTime= datetime.utcnow(),
                Statistics=[
                    'Average',
                ],
                Unit='Percent',
                Period=86460,
                Dimensions=[
                    {
                    'Name': 'InstanceId',
                    'Value': instance_id
                    },
                ]
            )
        
            print('\t EC2 CPU  Credit Usage: ', CPUCreditUsage['Datapoints'][0]['Average'], '%')
            print('\t EC2 CPU Utilization', CPUUtilization['Datapoints'][0]['Average'], '%')

            print('-'*60)

        except Exception as error:
            handleError(error)

    def setAlarm(self):
        print(f'EC2 CPU (last 30 min) information')

        try:
            EC2(self.user).list_instances()
            instance_id = input("Provide an instance id: ")

            self.cloudwatch.put_metric_alarm(
                AlarmName='EC2_CPU_Utilization_' + instance_id,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='CPUUtilization',
                Namespace='AWS/EC2',
                Period=60,
                Statistic='Average',
                Threshold=45.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when server CPU exceeds 70%',
                Dimensions=[
                    {
                    'Name': 'InstanceId',
                    'Value': instance_id
                    },
                ],
                Unit='Seconds'
            )

            print('Alarm created successfully')

        except Exception as error:
            handleError(error)