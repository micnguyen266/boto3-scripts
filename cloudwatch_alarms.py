import os
import sys
import boto3

# To Run Script
# 1. Input your values under REQUIRED
# 2. Run: python cloudwatch_alarms.py

# ================================================================================================================
# AWS Profiles Function (Do not touch!)
# ================================================================================================================


def awsProfiles():
    # User Input AWS Profile
    print()
    print("Your AWS Profiles:")
    print()

    for profile in boto3.session.Session().available_profiles:
        print(profile)

    print()
    aws_profile = input("Enter Desired AWS Profile: ")
    os.environ["AWS_PROFILE"] = aws_profile
    print(os.environ["AWS_PROFILE"])
    print()


awsProfiles()

client = boto3.client("sts")
account_id = client.get_caller_identity()["Account"]


# ================================================================================================================
# Region Menu Function (Do not touch!)
# ================================================================================================================


def regionMenu():
    print()
    print("Select AWS Region")
    print()
    print("     [1] us-east-1")
    print("     [2] us-east-2")
    print("     [3] eu-central-1")
    print("     [4] ap-southeast-2")
    print("     [5] ap-northeast-1")
    print("     [6] sa-east-1")
    print("     [7] us-gov-west-1")
    print("     [0] Exit the script.")


def regionMain():
    regionMenu()
    print()
    regionOption = int(input("Enter your option: "))
    print()

    while regionOption != 0:
        if regionOption == 1:
            regionName = 'us-east-1'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 2:
            regionName = 'us-east-2'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 3:
            regionName = 'eu-central-1'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 4:
            regionName = 'ap-southeast-2'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 5:
            regionName = 'ap-northeast-1'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 6:
            regionName = 'sa-east-1'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        elif regionOption == 7:
            regionName = 'us-gov-west-1'
            print(regionName, "has been selected")
            input("Press Enter to continue...")
            return regionName
        else:
            print()
            print(regionOption, "is an invalid option.")
            input("Press Enter to continue...")
            print()

        regionMenu()
        print()
        regionOption = int(input("Enter your option: "))
        print()

    print("Thanks for using this script. Goodbye.")
    exit()


region = regionMain()
cloudwatch = boto3.client('cloudwatch', region_name=region)


# def reset_Region():
#     global region
#     del region
#     global cloudwatch
#     del cloudwatch
#     region = regionMain()
#     cloudwatch = boto3.client('cloudwatch', region_name=region)


# ================================================================================================================
# PLEASE INPUT YOUR VALUES BELOW! (REQUIRED!!!)
# ================================================================================================================


# Specify AWS account (Part of Naming Convention of CloudWatch Alarm)
account_name = 'Prod'

# ========================================================
# EC2
# ========================================================

# Specify EC2 instances that needs CloudWatch monitoring
ec2_instances = ['i-abc123']

# Multiple EC2 example
# ec2_instances = ['i-abc456', 'i-abc789']

# EC2 Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
ec2_cpu_ComparisonOperator = 'GreaterThanThreshold'

# Threshold for EC2 CPU Utilization
ec2_cpu_threshold = 90

# EC2 Datapoints to Alarm (Evaluation Period)
ec2_cpu_EvaluationPeriods = 5

# EC2 Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
ec2_cpu_TreatMissingData = 'notBreaching'

# ========================================================
# ECS Cluster
# ========================================================

# Please put the ECS ClusterName and ServiceName
ecs_clusternames = ['testcluster']
ecs_servicenames = 'testservice'

# ECS Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
ecs_runningtask_ComparisonOperator = 'LessThanOrEqualToThreshold'
ecs_pendingtask_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_networkRX_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_networkTX_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_cpures_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_memres_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_cpuutil_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_memutil_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_servicecount_ComparisonOperator = 'LessThanThreshold'

# ECS Thresholds
ecs_runningtask_threshold = 0
ecs_pendingtask_threshold = 20
ecs_networkrxbytes_threshold = 180000000
ecs_networktxbytes_threshold = 140000000
ecs_cpures_threshold = 350
ecs_memres_threshold = 300
ecs_cpuutil_threshold = 350
ecs_memutil_threshold = 500
ecs_servicecount_threshold = 1

# ECS Datapoints to Alarm (Evaluation Period)
ecs_runningtask_EvaluationPeriods = 5
ecs_pendingtask_EvaluationPeriods = 5
ecs_networkRX_EvaluationPeriods = 5
ecs_networkTX_EvaluationPeriods = 5
ecs_cpures_EvaluationPeriods = 2
ecs_memres_EvaluationPeriods = 2
ecs_cpuutil_EvaluationPeriods = 5
ecs_memutil_EvaluationPeriods = 5
ecs_servicecount_EvaluationPeriods = 5

# ECS Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
ecs_runningtask_TreatMissingData = 'notBreaching'
ecs_pendingtask_TreatMissingData = 'notBreaching'
ecs_networkRX_TreatMissingData = 'notBreaching'
ecs_networkTX_TreatMissingData = 'notBreaching'
ecs_cpures_TreatMissingData = 'notBreaching'
ecs_memres_TreatMissingData = 'notBreaching'
ecs_cpuutil_TreatMissingData = 'notBreaching'
ecs_memutil_TreatMissingData = 'notBreaching'
ecs_servicecount_TreatMissingData = 'notBreaching'

# ========================================================
# DynamoDB Table
# ========================================================

# DynamoDB Table Name
dynamodb_tablenames = ['testtable']

# Used with successfulrequestlatency metric
dynamodb_table_operation = 'GetItem'

# DynamoDB Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
dynamodb_table_srl_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
dynamodb_table_writecap_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
dynamodb_table_readcap_ComparisonOperator = 'GreaterThanOrEqualToThreshold'

# DynamoDB Table Thresholds
successfulrequestlatency_threshold = 70
consumedwritecapacityunits_threshold = 70
consumedreadcapacityunits_threshold = 70

# DynamoDB Table Datapoints to Alarm (Evaluation Period)
dynamodb_table_srl_EvaluationPeriods = 3
dynamodb_table_writecap_EvaluationPeriods = 3
dynamodb_table_readcap_EvaluationPeriods = 3

# DynamoDB Table Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
dynamodb_table_srl_TreatMissingData = 'notBreaching'
dynamodb_table_writecap_TreatMissingData = 'breaching'
dynamodb_table_readcap_TreatMissingData = 'breaching'

# ========================================================
# ALB/ELB/NLB
# ========================================================

# LoadBalancer Name
lb_names = ['net/test']

# LB TargetGroup
lb_targetgroup = 'targetgroup/test'

# LB Namespace
lb_namespace = 'AWS/NetworkELB'

# LB Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
lb_HTTPCode_Target_4XX_Count_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
lb_HTTPCode_Target_5XX_Count_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
lb_unhealthyhostcount_ComparisonOperator = 'GreaterThanOrEqualToThreshold'

# LB Thresholds
lb_HTTPCode_Target_4XX_Count_threshold = 50
lb_HTTPCode_Target_5XX_Count_threshold = 50
lb_unhealthyhostcount_threshold = 2

# LB Datapoints to Alarm (Evaluation Period)
lb_HTTPCode_Target_4XX_Count_EvaluationPeriods = 3
lb_HTTPCode_Target_5XX_Count_EvaluationPeriods = 3
lb_unhealthyhostcount_EvaluationPeriods = 3

# LB Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
lb_HTTPCode_Target_4XX_Count_TreatMissingData = 'notBreaching'
lb_HTTPCode_Target_5XX_Count_TreatMissingData = 'notBreaching'
lb_unhealthyhostcount_TreatMissingData = 'missing'

# LB Statistic
lb_HTTPCode_Target_4XX_Count_statistic = 'Sum'
lb_HTTPCode_Target_5XX_Count_statistic = 'Sum'
lb_unhealthyhostcount_statistic = 'Average'

# ========================================================
# Kinesis
# ========================================================

# Kinesis Name
kinesis_streamNames = ['teststream']

# Kinesis Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
kinesis_WriteProvision_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
kinesis_ReadProvision_ComparisonOperator = 'GreaterThanOrEqualToThreshold'

# Kinesis Thresholds
kinesis_WriteProvision_threshold = 25
kinesis_ReadProvision_threshold = 25

# Kinesis Datapoints to Alarm (Evaluation Period)
kinesis_WriteProvision_EvaluationPeriods = 2
kinesis_ReadProvision_EvaluationPeriods = 3

# Kinesis Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
kinesis_WriteProvision_TreatMissingData = 'notBreaching'
kinesis_ReadProvision_TreatMissingData = 'missing'

# Kinesis Statistic
kinesis_WriteProvision_statistic = 'Sum'
kinesis_ReadProvision_statistic = 'Average'

# ========================================================
# Lambda
# ========================================================

# Lambda Name
lambda_functionNames = ['lambda-test']

# Lambda Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
lambda_errors_ComparisonOperator = 'GreaterThanThreshold'
lambda_throttles_ComparisonOperator = 'GreaterThanThreshold'
lambda_duration_ComparisonOperator = 'GreaterThanThreshold'
lambda_iterator_ComparisonOperator = 'GreaterThanThreshold'

# Lambda Thresholds
lambda_errors_threshold = 50
lambda_throttles_threshold = 5
lambda_duration_threshold = 5000
lambda_iterator_threshold = 3000

# Lambda Datapoints to Alarm (Evaluation Period)
lambda_errors_EvaluationPeriods = 5
lambda_throttles_EvaluationPeriods = 5
lambda_duration_EvaluationPeriods = 5
lambda_iterator_EvaluationPeriods = 5

# Lambda Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
lambda_errors_TreatMissingData = 'notBreaching'
lambda_throttles_TreatMissingData = 'notBreaching'
lambda_duration_TreatMissingData = 'notBreaching'
lambda_iterator_TreatMissingData = 'notBreaching'

# Lambda Statistic
lambda_errors_statistic = 'Average'
lambda_throttles_statistic = 'Average'
lambda_duration_statistic = 'Average'
lambda_iterator_statistic = 'Average'

# ========================================================
# Elasticache
# ========================================================

# Elasticache CacheClusterId
elasticache_CacheClusterIds = ['test1', 'test2']

# Elasticache CacheNodeId
elasticache_CacheNodeId = 'test'

# Elasticache Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
elasticache_cpu_ComparisonOperator = 'GreaterThanOrEqualToThreshold'

# Elasticache Thresholds
elasticache_cpu_threshold = 90

# Elasticache Datapoints to Alarm (Evaluation Period)
elasticache_cpu_EvaluationPeriods = 2

# Elasticache Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
elasticache_cpu_TreatMissingData = 'missing'

# Elasticache Statistic
elasticache_cpu_statistic = 'Average'

# Elasticache Period (in seconds)
elasticache_cpu_period = 600

# ========================================================
# SNS Topic (REQUIRED!!!)
# ========================================================

# Specify existing SNS Topic(s) (In Alarm and OK notifications will both be created)
sns_topic_name = 'test1'
sns_topic_name2 = 'test2'
sns_topic_name3 = 'test3'

# Do not touch!
alarm_sns = 'arn:aws:sns:{}:{}:{}'.format(region, account_id, sns_topic_name)
alarm_sns2 = 'arn:aws:sns:{}:{}:{}'.format(region, account_id, sns_topic_name2)
alarm_sns3 = 'arn:aws:sns:{}:{}:{}'.format(region, account_id, sns_topic_name3)

# Comment/Uncomment if you want 1/2/3 SNS topics below as necessary.
# E.g. [alarm_sns, alarm_sns2, alarm_sns3], [alarm_sns, alarm_sns2] or [alarm_sns]
# allAlarmActions = [alarm_sns]
# allAlarmActions = [alarm_sns, alarm_sns2]
allAlarmActions = [alarm_sns, alarm_sns2, alarm_sns3]
# allOKActions = [alarm_sns]
# allOKActions = [alarm_sns, alarm_sns2]
allOKActions = [alarm_sns, alarm_sns2, alarm_sns3]

# ================================================================================================================
# CloudWatch Functions (Do not touch!)
# ================================================================================================================


def createCloudwatchEC2():
    for ec2_instance in ec2_instances:
        cloudwatch.put_metric_alarm(
            AlarmName='EC2 {} - CPU Utilization above {}% ({}-{})'.format(ec2_instance, ec2_cpu_threshold, region,
                                                                          account_name),
            ComparisonOperator=ec2_cpu_ComparisonOperator,
            EvaluationPeriods=ec2_cpu_EvaluationPeriods,
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Period=300,
            Statistic='Average',
            Threshold=ec2_cpu_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when server CPU Utilization exceeds 90%',
            TreatMissingData=ec2_cpu_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': ec2_instance
                },
            ],
        )
    # for ec2_instance in ec2_instances:
    #     cloudwatch.put_metric_alarm(
    #         AlarmName='EC2-{} - Memory Utilized above {}% ({}-{})'.format(ec2_instance, ec2_cpu_threshold, region, account_name),
    #         ComparisonOperator='GreaterThanThreshold',
    #         EvaluationPeriods=1,
    #         MetricName='MemoryUtilized',
    #         Namespace='AWS/EC2',
    #         Period=300,
    #         Statistic='Average',
    #         Threshold=90.0,
    #         ActionsEnabled=True,
    #         AlarmActions = allAlarmActions,
    #         OKActions = allOKActions,
    #         AlarmDescription='Alerts when server CPU exceeds 90%',
    #         Dimensions=[
    #             {
    #                 'Name': 'InstanceId',
    #                 'Value': ec2_instance
    #             },
    #         ],
    #     )
    print('EC2 alarms Created For:', ec2_instances)


def deleteCloudwatchEC2():
    for ec2_instance in ec2_instances:
        cloudwatch.delete_alarms(
            AlarmNames=['EC2 {} - CPU Utilization above {}% ({}-{})'.format(ec2_instance, ec2_cpu_threshold, region,
                                                                            account_name)],
        )
    print('EC2 alarms Deleted:', ec2_instances)


# # DISABLED until needed
# # List alarms of insufficient data through the pagination interface
# # def describeCloudwatchEC2():
#     paginator = cloudwatch.get_paginator('describe_alarms')
#     for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
#         print(response['MetricAlarms'])


def createCloudwatchECS():
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-RunningTaskCount ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_runningtask_ComparisonOperator,
            EvaluationPeriods=ecs_runningtask_EvaluationPeriods,
            MetricName='RunningTaskCount',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_runningtask_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_runningtask_ComparisonOperator, ecs_runningtask_threshold),
            TreatMissingData=ecs_runningtask_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-PendingTaskCount ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_pendingtask_ComparisonOperator,
            EvaluationPeriods=ecs_pendingtask_EvaluationPeriods,
            MetricName='PendingTaskCount',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_pendingtask_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Pending Task Count is {} to {}'.format(
                ecs_pendingtask_ComparisonOperator, ecs_pendingtask_threshold),
            TreatMissingData=ecs_pendingtask_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-NetworkRXBytes ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_networkRX_ComparisonOperator,
            EvaluationPeriods=ecs_networkRX_EvaluationPeriods,
            MetricName='NetworkRxBytes',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_networkrxbytes_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when NetworkRXBytes is {} to {}'.format(
                ecs_networkRX_ComparisonOperator, ecs_networkrxbytes_threshold),
            TreatMissingData=ecs_networkRX_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )

    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-NetworkTXBytes ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_networkTX_ComparisonOperator,
            EvaluationPeriods=ecs_networkTX_EvaluationPeriods,
            MetricName='NetworkTxBytes',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_networktxbytes_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Network_TX_Bytes is {} to {}'.format(
                ecs_networkTX_ComparisonOperator, ecs_networktxbytes_threshold),
            TreatMissingData=ecs_networkTX_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-CPUReserved ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_cpures_ComparisonOperator,
            EvaluationPeriods=ecs_cpures_EvaluationPeriods,
            MetricName='CpuReserved',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_cpures_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_cpures_ComparisonOperator, ecs_cpures_threshold),
            TreatMissingData=ecs_cpures_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-MemoryReserved ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_memres_ComparisonOperator,
            EvaluationPeriods=ecs_memres_EvaluationPeriods,
            MetricName='MemoryReserved',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_memres_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_memres_ComparisonOperator, ecs_memres_threshold),
            TreatMissingData=ecs_memres_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-CPUUtilization ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_cpuutil_ComparisonOperator,
            EvaluationPeriods=ecs_cpuutil_EvaluationPeriods,
            MetricName='CpuUtilized',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_cpuutil_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_cpuutil_ComparisonOperator, ecs_cpuutil_threshold),
            TreatMissingData=ecs_cpuutil_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-MemoryUtilized ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_memutil_ComparisonOperator,
            EvaluationPeriods=ecs_memutil_EvaluationPeriods,
            MetricName='MemoryUtilized',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_memutil_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_memutil_ComparisonOperator, ecs_memutil_threshold),
            TreatMissingData=ecs_memutil_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    for ecs_clustername in ecs_clusternames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-ServiceCount ({}-{})'.format(ecs_servicenames, region, account_name),
            ComparisonOperator=ecs_servicecount_ComparisonOperator,
            EvaluationPeriods=ecs_servicecount_EvaluationPeriods,
            MetricName='ServiceCount',
            Namespace='ECS/ContainerInsights',
            Period=300,
            Statistic='Average',
            Threshold=ecs_servicecount_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Running Task Count is {} to {}'.format(
                ecs_servicecount_ComparisonOperator, ecs_servicecount_threshold),
            TreatMissingData=ecs_servicecount_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'ClusterName',
                    'Value': ecs_clustername
                },
                {
                    'Name': 'ServiceName',
                    'Value': ecs_servicenames
                },
            ],
        )
    print('ECS alarms Created For ClusterName:', ecs_clusternames, 'ServiceName:', ecs_servicenames)


def deleteCloudwatchECS():
    for ecs_servicename in ecs_servicenames:
        cloudwatch.delete_alarms(
            AlarmNames=[
                '{}-RunningTaskCount ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-PendingTaskCount ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-NetworkTXBytes ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-NetworkRXBytes ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-CPUReservation ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-MemoryReserved ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-CPUUtilization ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-MemoryUtilized ({}-{})'.format(ecs_servicename, region, account_name),
                '{}-ServiceCount ({}-{})'.format(ecs_servicename, region, account_name)],
        )
    print('ECS alarms Deleted For ClusterName:', ecs_clusternames, 'ServiceName:', ecs_servicenames)


def createCloudwatchDynamoDBTable():
    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-SuccessfulRequestLatency ({}-{})'.format(
                dynamodb_tablename, region, account_name),
            ComparisonOperator=dynamodb_table_srl_ComparisonOperator,
            EvaluationPeriods=dynamodb_table_srl_EvaluationPeriods,
            MetricName='SuccessfulRequestLatency',
            Namespace='AWS/DynamoDB',
            Period=300,
            Statistic='Average',
            Threshold=successfulrequestlatency_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when DynamoDB table {} successful request latency is {} to {} Milliseconds'.format(
                dynamodb_table_operation, dynamodb_table_srl_ComparisonOperator, successfulrequestlatency_threshold),
            TreatMissingData=dynamodb_table_srl_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'TableName',
                    'Value': dynamodb_tablename
                },
            ],
        )

    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-ConsumedWriteCapacityUnits ({}-{})'.format(
                dynamodb_tablename, region, account_name),
            ComparisonOperator=dynamodb_table_writecap_ComparisonOperator,
            EvaluationPeriods=dynamodb_table_writecap_EvaluationPeriods,
            MetricName='ConsumedWriteCapacityUnits',
            Namespace='AWS/DynamoDB',
            Period=300,
            Statistic='Average',
            Threshold=consumedwritecapacityunits_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when DynamoDB table consumed write capacity is {} to {} units'.format(
                dynamodb_table_writecap_ComparisonOperator, consumedwritecapacityunits_threshold),
            TreatMissingData=dynamodb_table_writecap_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'TableName',
                    'Value': dynamodb_tablename
                },
            ],
        )

    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-ConsumedReadCapacityUnits ({}-{})'.format(
                dynamodb_tablename, region, account_name),
            ComparisonOperator=dynamodb_table_readcap_ComparisonOperator,
            EvaluationPeriods=dynamodb_table_readcap_EvaluationPeriods,
            MetricName='ConsumedReadCapacityUnits',
            Namespace='AWS/DynamoDB',
            Period=300,
            Statistic='Average',
            Threshold=consumedreadcapacityunits_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when DynamoDB table consumed read capacity is {} to {} units'.format(
                dynamodb_table_readcap_ComparisonOperator, consumedreadcapacityunits_threshold),
            TreatMissingData=dynamodb_table_readcap_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'TableName',
                    'Value': dynamodb_tablename
                },
            ],
        )
    print('DynamoDB Table alarms Created For TableName:', dynamodb_tablenames)


def deleteCloudwatchDynamoDBTable():
    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.delete_alarms(
            AlarmNames=[
                '{}-SuccessfulRequestLatency ({}-{})'.format(dynamodb_tablename, region, account_name),
                '{}-ConsumedWriteCapacityUnits ({}-{})'.format(dynamodb_tablename, region, account_name),
                '{}-ConsumedReadCapacityUnits ({}-{})'.format(dynamodb_tablename, region, account_name)],
        )
    print('DynamoDB Tables alarms Deleted For TableName:', dynamodb_tablenames)


def createCloudwatchLB():
    for lb_name in lb_names:
        cloudwatch.put_metric_alarm(
            AlarmName='ALB - {} - HTTPCode_Target_4XX_Count above or equal {} ({}-{})'.format(lb_name,
                                                                                              lb_HTTPCode_Target_4XX_Count_threshold,
                                                                                              region, account_name),
            ComparisonOperator=lb_HTTPCode_Target_4XX_Count_ComparisonOperator,
            EvaluationPeriods=lb_HTTPCode_Target_4XX_Count_EvaluationPeriods,
            MetricName='HTTPCode_Target_4XX_Count',
            Namespace=lb_namespace,
            Period=300,
            Statistic=lb_HTTPCode_Target_4XX_Count_statistic,
            Threshold=lb_HTTPCode_Target_4XX_Count_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when ALB {} HTTPCode_Target_4XX_Count is above or equal {} Count'.format(
                lb_name, lb_HTTPCode_Target_4XX_Count_threshold),
            TreatMissingData=lb_HTTPCode_Target_4XX_Count_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'LoadBalancer',
                    'Value': lb_name
                },
                {
                    'Name': 'TargetGroup',
                    'Value': lb_targetgroup
                },
            ],
        )
    for lb_name in lb_names:
        cloudwatch.put_metric_alarm(
            AlarmName='ALB - {} - HTTPCode_Target_5XX_Count above or equal {} ({}-{})'.format(lb_name,
                                                                                              lb_HTTPCode_Target_5XX_Count_threshold,
                                                                                              region, account_name),
            ComparisonOperator=lb_HTTPCode_Target_5XX_Count_ComparisonOperator,
            EvaluationPeriods=lb_HTTPCode_Target_5XX_Count_EvaluationPeriods,
            MetricName='HTTPCode_Target_5XX_Count',
            Namespace=lb_namespace,
            Period=300,
            Statistic=lb_HTTPCode_Target_5XX_Count_statistic,
            Threshold=lb_HTTPCode_Target_5XX_Count_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when ALB {} HTTPCode_Target_5XX_Count is above or equal {} Count'.format(
                lb_name, lb_HTTPCode_Target_5XX_Count_threshold),
            TreatMissingData=lb_HTTPCode_Target_5XX_Count_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'LoadBalancer',
                    'Value': lb_name
                },
                {
                    'Name': 'TargetGroup',
                    'Value': lb_targetgroup
                },
            ],
        )
    for lb_name in lb_names:
        cloudwatch.put_metric_alarm(
            AlarmName='ALB - {} - unhealthy host count above or equal {} ({}-{})'.format(lb_name,
                                                                                         lb_unhealthyhostcount_threshold,
                                                                                         region, account_name),
            ComparisonOperator=lb_unhealthyhostcount_ComparisonOperator,
            EvaluationPeriods=lb_unhealthyhostcount_EvaluationPeriods,
            MetricName='UnHealthyHostCount',
            Namespace=lb_namespace,
            Period=300,
            Statistic=lb_unhealthyhostcount_statistic,
            Threshold=lb_unhealthyhostcount_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when ALB {} unhealthy host count is above or equal {} Count'.format(lb_name,
                                                                                                         lb_unhealthyhostcount_threshold),
            TreatMissingData=lb_unhealthyhostcount_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'LoadBalancer',
                    'Value': lb_name
                },
                {
                    'Name': 'TargetGroup',
                    'Value': lb_targetgroup
                },
            ],
        )
    print('LB alarms Created For LoadBalancer:', lb_names)


def deleteCloudwatchLB():
    for lb_name in lb_names:
        cloudwatch.delete_alarms(
            AlarmNames=[
                'ALB - {} - HTTPCode_Target_4XX_Count above or equal {} ({}-{})'.format(lb_name,
                                                                                        lb_HTTPCode_Target_4XX_Count_threshold,
                                                                                        region, account_name),
                'ALB - {} - HTTPCode_Target_5XX_Count above or equal {} ({}-{})'.format(lb_name,
                                                                                        lb_HTTPCode_Target_5XX_Count_threshold,
                                                                                        region, account_name),
                'ALB - {} - unhealthy host count above or equal {} ({}-{})'.format(lb_name,
                                                                                   lb_unhealthyhostcount_threshold,
                                                                                   region, account_name), ],
        )
    print('LB alarms Deleted For Load Balancer:', lb_names)


def createCloudwatchKinesis():
    for kinesis_streamName in kinesis_streamNames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-ReadProvisionedThroughputExceeded ({}-{})'.format(
                kinesis_streamName, region, account_name),
            ComparisonOperator=kinesis_ReadProvision_ComparisonOperator,
            EvaluationPeriods=kinesis_ReadProvision_EvaluationPeriods,
            MetricName='ReadProvisionedThroughputExceeded',
            Namespace='AWS/Kinesis',
            Period=300,
            Statistic=kinesis_ReadProvision_statistic,
            Threshold=kinesis_ReadProvision_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Kinesis {} ReadProvisionedThroughputExceeded is above or equal {} Count'.format(
                kinesis_streamName, kinesis_ReadProvision_threshold),
            TreatMissingData=kinesis_ReadProvision_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'StreamName',
                    'Value': kinesis_streamName
                },
            ],
        )
    for kinesis_streamName in kinesis_streamNames:
        cloudwatch.put_metric_alarm(
            AlarmName='{}-WriteProvisionedThroughputExceeded ({}-{})'.format(
                kinesis_streamName, region, account_name),
            ComparisonOperator=kinesis_WriteProvision_ComparisonOperator,
            EvaluationPeriods=kinesis_WriteProvision_EvaluationPeriods,
            MetricName='WriteProvisionedThroughputExceeded',
            Namespace='AWS/Kinesis',
            Period=300,
            Statistic=kinesis_WriteProvision_statistic,
            Threshold=kinesis_WriteProvision_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Kinesis {} WriteProvisionedThroughputExceeded is above or equal {} Count'.format(
                kinesis_streamName, kinesis_WriteProvision_threshold),
            TreatMissingData=kinesis_WriteProvision_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'StreamName',
                    'Value': kinesis_streamName
                },
            ],
        )
    print('Kinesis alarms Created For StreamName:', kinesis_streamNames)


def deleteCloudwatchKinesis():
    for kinesis_streamName in kinesis_streamNames:
        cloudwatch.delete_alarms(
            AlarmNames=[
                'Kinesis - {} - ReadProvisionedThroughputExceeded above or equal {} ({}-{})'.format(kinesis_streamName,
                                                                                                    kinesis_ReadProvision_threshold,
                                                                                                    region,
                                                                                                    account_name),
                'Kinesis - {} - WriteProvisionedThroughputExceeded above or equal {} ({}-{})'.format(kinesis_streamName,
                                                                                                     kinesis_WriteProvision_threshold,
                                                                                                     region,
                                                                                                     account_name), ],
        )
    print('Kinesis alarms Deleted For StreamName:', kinesis_streamNames)


def createCloudwatchLambda():
    for lambda_functionName in lambda_functionNames:
        cloudwatch.put_metric_alarm(
            AlarmName='Lambda - {} - Errors ({}-{})'.format(
                lambda_functionName,region, account_name),
            ComparisonOperator=lambda_errors_ComparisonOperator,
            EvaluationPeriods=lambda_errors_EvaluationPeriods,
            MetricName='Errors',
            Namespace='AWS/Lambda',
            Period=300,
            Statistic=lambda_errors_statistic,
            Threshold=lambda_errors_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Lambda {} Errors is {} to {}'.format(
                lambda_functionName, lambda_errors_ComparisonOperator, lambda_errors_threshold),
            TreatMissingData=lambda_errors_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'FunctionName',
                    'Value': lambda_functionName
                },
            ],
        )
    for lambda_functionName in lambda_functionNames:
        cloudwatch.put_metric_alarm(
            AlarmName='Lambda - {} - Throttles ({}-{})'.format(
                lambda_functionName, region, account_name),
            ComparisonOperator=lambda_throttles_ComparisonOperator,
            EvaluationPeriods=lambda_throttles_EvaluationPeriods,
            MetricName='Throttles',
            Namespace='AWS/Lambda',
            Period=300,
            Statistic=lambda_throttles_statistic,
            Threshold=lambda_throttles_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Lambda {} Throttles is {} to {}'.format(
                lambda_functionName, lambda_throttles_ComparisonOperator, lambda_throttles_threshold),
            TreatMissingData=lambda_throttles_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'FunctionName',
                    'Value': lambda_functionName
                },
            ],
        )
    for lambda_functionName in lambda_functionNames:
        cloudwatch.put_metric_alarm(
            AlarmName='Lambda - {} - Duration ({}-{})'.format(
                lambda_functionName, region, account_name),
            ComparisonOperator=lambda_duration_ComparisonOperator,
            EvaluationPeriods=lambda_duration_EvaluationPeriods,
            MetricName='Duration',
            Namespace='AWS/Lambda',
            Period=300,
            Statistic=lambda_duration_statistic,
            Threshold=lambda_duration_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Lambda {} Duration is {} to {}'.format(
                lambda_functionName, lambda_duration_ComparisonOperator, lambda_duration_threshold),
            TreatMissingData=lambda_duration_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'FunctionName',
                    'Value': lambda_functionName
                },
            ],
        )
    for lambda_functionName in lambda_functionNames:
        cloudwatch.put_metric_alarm(
            AlarmName='Lambda - {} - IteratorAge ({}-{})'.format(
                lambda_functionName, region, account_name),
            ComparisonOperator=lambda_iterator_ComparisonOperator,
            EvaluationPeriods=lambda_iterator_EvaluationPeriods,
            MetricName='IteratorAge',
            Namespace='AWS/Lambda',
            Period=300,
            Statistic=lambda_iterator_statistic,
            Threshold=lambda_iterator_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Lambda {} IteratorAge is {} to {}'.format(
                lambda_functionName, lambda_iterator_ComparisonOperator, lambda_iterator_threshold),
            TreatMissingData=lambda_iterator_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'FunctionName',
                    'Value': lambda_functionName
                },
            ],
        )
    print('Lambda alarms Created For FunctionName:', lambda_functionNames)


def deleteCloudwatchLambda():
    for lambda_functionName in lambda_functionNames:
        cloudwatch.delete_alarms(
            AlarmNames=[
                'Lambda - {} - Errors ({}-{})'.format(lambda_functionName,region, account_name),
                'Lambda - {} - Throttles ({}-{})'.format(lambda_functionName, region, account_name),
                'Lambda - {} - Duration ({}-{})'.format(lambda_functionName, region, account_name),
                'Lambda - {} - IteratorAge ({}-{})'.format(lambda_functionName, region, account_name)],
        )
    print('Lambda alarms Deleted For FunctionName:', lambda_functionNames)


def createCloudwatchElasticache():
    for elasticache_CacheClusterId in elasticache_CacheClusterIds:
        cloudwatch.put_metric_alarm(
            AlarmName='Elasticache Redis - {} - CPU Utilization above {}% ({}-{})'.format(
                elasticache_CacheClusterId, elasticache_cpu_threshold, region, account_name),
            ComparisonOperator=elasticache_cpu_ComparisonOperator,
            EvaluationPeriods=elasticache_cpu_EvaluationPeriods,
            MetricName='CPUUtilization',
            Namespace='AWS/ElastiCache',
            Period=elasticache_cpu_period,
            Statistic=elasticache_cpu_statistic,
            Threshold=elasticache_cpu_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when Elasticache {} CPU Utilization above {}%'.format(
                elasticache_CacheClusterId, elasticache_cpu_threshold),
            TreatMissingData=elasticache_cpu_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'CacheClusterId',
                    'Value': elasticache_CacheClusterId
                },
                {
                    'Name': 'CacheNodeId',
                    'Value': elasticache_CacheNodeId
                },
            ],
        )
    print('Elasticache alarms Created For CacheClusterId:', elasticache_CacheClusterIds)


def deleteCloudwatchElasticache():
    for elasticache_CacheClusterId in elasticache_CacheClusterIds:
        cloudwatch.delete_alarms(
            AlarmNames=[
                'Elasticache Redis - {} - CPU Utilization above {}% ({}-{})'.format(elasticache_CacheClusterId,
                                                                                    elasticache_cpu_threshold, region,
                                                                                    account_name)],
        )
    print('Elasticache alarms Deleted For CacheClusterId:', elasticache_CacheClusterIds)


# ================================================================================================================
# Main Function (Do not touch!)
# ================================================================================================================


def menu():
    print()
    print("Script to Create/Delete CloudWatch Alarms")
    print()
    print("     [1] Create EC2 CPUUtilization CloudWatch Alarm(s)")
    print("     [2] Delete EC2 CPUUtilization CloudWatch Alarm(s)")
    print("     [3] Create ECS CPU/Mem/Run/PendTasks/NetworkRX/TX CloudWatch Alarm(s)")
    print("     [4] Delete ECS CPU/Mem/Run/PendTasks/NetworkRX/TX CloudWatch Alarm(s)")
    print("     [5] Create DynamoDB Table CloudWatch Alarm(s)")
    print("     [6] Delete DynamoDB Table CloudWatch Alarm(s)")
    print("     [7] Create Load Balancer CloudWatch Alarm(s)")
    print("     [8] Delete Load Balancer CloudWatch Alarm(s)")
    print("     [9] Create Kinesis CloudWatch Alarm(s)")
    print("     [10] Delete Kinesis CloudWatch Alarm(s)")
    print("     [11] Create Lambda CloudWatch Alarm(s)")
    print("     [12] Delete Lambda CloudWatch Alarm(s)")
    print("     [13] Create Elasticache CloudWatch Alarm(s)")
    print("     [14] Delete Elasticache CloudWatch Alarm(s)")
    print("     [15] Create All CloudWatch Alarm(s)")
    print("     [16] Delete All CloudWatch Alarm(s)")
    print("     [17] Restart Script. Deletes Variables from Memory.")
    print("     [0] Exit the script")


def main():
    menu()
    print()
    option = int(input("Enter your option: "))
    print()

    while option != 0:
        if option == 1:
            createCloudwatchEC2()
            input("Press Enter to continue...")
        elif option == 2:
            deleteCloudwatchEC2()
            input("Press Enter to continue...")
        elif option == 3:
            createCloudwatchECS()
            input("Press Enter to continue...")
        elif option == 4:
            deleteCloudwatchECS()
            input("Press Enter to continue...")
        elif option == 5:
            createCloudwatchDynamoDBTable()
            input("Press Enter to continue...")
        elif option == 6:
            deleteCloudwatchDynamoDBTable()
            input("Press Enter to continue...")
        elif option == 7:
            createCloudwatchLB()
            input("Press Enter to continue...")
        elif option == 8:
            deleteCloudwatchLB()
            input("Press Enter to continue...")
        elif option == 9:
            createCloudwatchKinesis()
            input("Press Enter to continue...")
        elif option == 10:
            deleteCloudwatchKinesis()
            input("Press Enter to continue...")
        elif option == 11:
            createCloudwatchLambda()
            input("Press Enter to continue...")
        elif option == 12:
            deleteCloudwatchLambda()
            input("Press Enter to continue...")
        elif option == 13:
            createCloudwatchElasticache()
            input("Press Enter to continue...")
        elif option == 14:
            deleteCloudwatchElasticache()
            input("Press Enter to continue...")
        elif option == 15:
            createCloudwatchEC2()
            createCloudwatchECS()
            createCloudwatchDynamoDBTable()
            createCloudwatchLB()
            createCloudwatchKinesis()
            createCloudwatchLambda()
            createCloudwatchElasticache()
            input("Press Enter to continue...")
        elif option == 16:
            deleteCloudwatchEC2()
            deleteCloudwatchECS()
            deleteCloudwatchDynamoDBTable()
            deleteCloudwatchLB()
            deleteCloudwatchKinesis()
            deleteCloudwatchLambda()
            deleteCloudwatchElasticache()
            input("Press Enter to continue...")
        elif option == 17:
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print()
            print(option, "is an invalid option.")
            input("Press Enter to continue...")
            print()

        menu()
        print()
        option = int(input("Enter your option: "))
        print()

    print("Thanks for using this script. Goodbye.")


main()

