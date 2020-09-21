import os
import boto3

# To Run Script
# 1. Input your values under REQUIRED
# 2. Run: python cloudwatch_alarms.py

# ================================================================================================================
# Environment Variables (Do not touch!)
# ================================================================================================================

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

# ================================================================================================================
# PLEASE INPUT YOUR VALUES BELOW! (REQUIRED!!!)
# ================================================================================================================

# Specify AWS account (Part of Naming Convention of CloudWatch Alarm)
account_name = 'Produdction'

# ========================================================
# EC2
# ========================================================

# Specify EC2 instances that needs CloudWatch monitoring
ec2_instances = ['i-abc123456789']

# Multiple EC2 example
# ec2_instances = ['i-abc123', 'i-abc456']

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
ecs_clusternames = ['ecs-clustername']
ecs_servicenames = 'ecs-servicename'

# ECS Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
ecs_cpumem_ComparisonOperator = 'GreaterThanThreshold'
ecs_runningtask_ComparisonOperator = 'LessThanOrEqualToThreshold'
ecs_pendingtask_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_networkRX_ComparisonOperator = 'GreaterThanOrEqualToThreshold'
ecs_networkTX_ComparisonOperator = 'GreaterThanOrEqualToThreshold'

# ECS Thresholds
ecs_cpumem_threshold = 90
ecs_runningtask_threshold = 0
ecs_pendingtask_threshold = 20
ecs_networkrxbytes_threshold = 500000000
ecs_networktxbytes_threshold = 500000000

# ECS Datapoints to Alarm (Evaluation Period)
ecs_cpumem_EvaluationPeriods = 5
ecs_runningtask_EvaluationPeriods = 5
ecs_pendingtask_EvaluationPeriods = 5
ecs_networkRX_EvaluationPeriods = 5
ecs_networkTX_EvaluationPeriods = 5

# ECS Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
ecs_cpumem_TreatMissingData = 'notBreaching'
ecs_runningtask_TreatMissingData = 'notBreaching'
ecs_pendingtask_TreatMissingData = 'notBreaching'
ecs_networkRX_TreatMissingData = 'notBreaching'
ecs_networkTX_TreatMissingData = 'notBreaching'

# ========================================================
# DynamoDB Table
# ========================================================

# DynamoDB Table Name
dynamodb_tablenames = ['dynamodb-tablename']

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
lb_names = ['app/test/12345']

# LB TargetGroup
lb_targetgroup = 'targetgroup/test/12345'

# LB Namespace
lb_namespace = 'AWS/ApplicationELB'

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
kinesis_streamNames = ['abc123test']

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
lambda_functionNames = ['lambdaname-test']

# Lambda Operators
# Options: GreaterThanThreshold, LessThanThreshold, LessThanOrEqualToThreshold, GreaterThanOrEqualToThreshold
lambda_errors_ComparisonOperator = 'GreaterThanThreshold'
lambda_throttles_ComparisonOperator = 'GreaterThanThreshold'

# Lambda Thresholds
lambda_errors_threshold = 1
lambda_throttles_threshold = 1

# Lambda Datapoints to Alarm (Evaluation Period)
lambda_errors_EvaluationPeriods = 3
lambda_throttles_EvaluationPeriods = 3

# Lambda Missing Data Treatment
# Options: breaching, notBreaching, ignore, missing
lambda_errors_TreatMissingData = 'missing'
lambda_throttles_TreatMissingData = 'missing'

# Lambda Statistic
lambda_errors_statistic = 'Average'
lambda_throttles_statistic = 'Average'

# ========================================================
# Elasticache
# ========================================================

# Elasticache CacheClusterId
elasticache_CacheClusterIds = ['clusterid001', 'clusterid002']

# Elasticache CacheNodeId
elasticache_CacheNodeId = '0001'

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
sns_topic_name = 'snstopic_test'
sns_topic_name2 = 'snstopic_test2'

# Do not touch!
alarm_sns = 'arn:aws:sns:{}:{}:{}'.format(region, account_id, sns_topic_name)
alarm_sns2 = 'arn:aws:sns:{}:{}:{}'.format(region, account_id, sns_topic_name2)

# Add/Remove 2nd SNS variable "alarm_sns2" below if necessary. E.g. [alarm_sns, alarm_sns2] or [alarm_sns]
allAlarmActions = [alarm_sns, alarm_sns2]
allOKActions = [alarm_sns, alarm_sns2]


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
            AlarmName='ecs-{} - CPU Utilization above {}% ({}-{})'.format(ecs_clustername, ecs_cpumem_threshold,
                                                                          region,
                                                                          account_name),
            ComparisonOperator=ecs_cpumem_ComparisonOperator,
            EvaluationPeriods=ecs_cpumem_EvaluationPeriods,
            MetricName='CPUUtilization',
            Namespace='AWS/ECS',
            Period=300,
            Statistic='Average',
            Threshold=ecs_cpumem_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when ECS CPU Utilization exceeds {}%'.format(ecs_cpumem_threshold),
            TreatMissingData=ecs_cpumem_TreatMissingData,
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
            AlarmName='ecs-{} - Memory Utilization above {}% ({}-{})'.format(ecs_clustername, ecs_cpumem_threshold,
                                                                             region, account_name),
            ComparisonOperator=ecs_cpumem_ComparisonOperator,
            EvaluationPeriods=ecs_cpumem_EvaluationPeriods,
            MetricName='MemoryUtilization',
            Namespace='AWS/ECS',
            Period=300,
            Statistic='Average',
            Threshold=ecs_cpumem_threshold,
            ActionsEnabled=True,
            AlarmActions=allAlarmActions,
            OKActions=allOKActions,
            AlarmDescription='Alerts when ECS Memory Utilization exceeds {}%'.format(ecs_cpumem_threshold),
            TreatMissingData=ecs_cpumem_TreatMissingData,
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
            AlarmName='ecs-{} - Running Task less than or equal to {} ({}-{})'.format(ecs_clustername,
                                                                                      ecs_runningtask_threshold,
                                                                                      region,
                                                                                      account_name),
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
            AlarmDescription='Alerts when Running Task Count is less than or equal to {}'.format(
                ecs_runningtask_threshold),
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
            AlarmName='ecs-{} - Pending Task greater than or equal to {} ({}-{})'.format(ecs_clustername,
                                                                                         ecs_pendingtask_threshold,
                                                                                         region, account_name),
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
            AlarmDescription='Alerts when Pending Task Count is greater than or equal to {}'.format(
                ecs_pendingtask_threshold),
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
            AlarmName='ecs-{} - Network_RX_Bytes ({}-{})'.format(ecs_clustername, region, account_name),
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
            AlarmDescription='Alerts when Network_RX_Bytes is greater than or equal to {}'.format(
                ecs_networkrxbytes_threshold),
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
            AlarmName='ecs-{} - Network_TX_Bytes ({}-{})'.format(ecs_clustername, region, account_name),
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
            AlarmDescription='Alerts when Network_TX_Bytes is greater than or equal to {}'.format(
                ecs_networktxbytes_threshold),
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
    print('ECS alarms Created For ClusterName:', ecs_clusternames, 'ServiceName:', ecs_servicenames)


def deleteCloudwatchECS():
    for ecs_clustername in ecs_clusternames:
        cloudwatch.delete_alarms(
            AlarmNames=[
                'ecs-{} - CPU Utilization above {}% ({}-{})'.format(ecs_clustername, ecs_cpumem_threshold, region,
                                                                    account_name),
                'ecs-{} - Memory Utilization above {}% ({}-{})'.format(ecs_clustername, ecs_cpumem_threshold,
                                                                       region,
                                                                       account_name),
                'ecs-{} - Running Task less than or equal to {} ({}-{})'.format(ecs_clustername,
                                                                                ecs_runningtask_threshold, region,
                                                                                account_name),
                'ecs-{} - Pending Task greater than or equal to {} ({}-{})'.format(ecs_clustername,
                                                                                   ecs_pendingtask_threshold,
                                                                                   region,
                                                                                   account_name),
                'ecs-{} - Network_RX_Bytes ({}-{})'.format(ecs_clustername, region, account_name),
                'ecs-{} - Network_TX_Bytes ({}-{})'.format(ecs_clustername, region, account_name), ],
        )
    print('ECS alarms Deleted For ClusterName:', ecs_clusternames, 'ServiceName:', ecs_servicenames)


def createCloudwatchDynamoDBTable():
    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.put_metric_alarm(
            AlarmName='dynamodb table {} - {} successful request latency above or equal {} ms ({}-{})'.format(
                dynamodb_tablename, dynamodb_table_operation, successfulrequestlatency_threshold, region,
                account_name),
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
            AlarmDescription='Alerts when DynamoDB table {} successful request latency is above or equal {} Milliseconds'.format(
                dynamodb_table_operation, successfulrequestlatency_threshold),
            TreatMissingData=dynamodb_table_srl_TreatMissingData,
            Dimensions=[
                {
                    'Name': 'TableName',
                    'Value': dynamodb_tablename
                },
                {
                    'Name': 'Operation',
                    'Value': dynamodb_table_operation
                },
            ],
        )

    for dynamodb_tablename in dynamodb_tablenames:
        cloudwatch.put_metric_alarm(
            AlarmName='dynamodb table {} - consumed write capacity above or equal {} units ({}-{})'.format(
                dynamodb_tablename, successfulrequestlatency_threshold, region, account_name),
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
            AlarmDescription='Alerts when DynamoDB table consumed write capacity is above or equal {} units'.format(
                consumedwritecapacityunits_threshold),
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
            AlarmName='dynamodb table {} - consumed read capacity above or equal {} units ({}-{})'.format(
                dynamodb_tablename, successfulrequestlatency_threshold, region, account_name),
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
            AlarmDescription='Alerts when DynamoDB table consumed read capacity is above or equal {} units'.format(
                consumedreadcapacityunits_threshold),
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
                'dynamodb table {} - {} successful request latency above or equal {} ms ({}-{})'.format(
                    dynamodb_tablename, dynamodb_table_operation, successfulrequestlatency_threshold, region,
                    account_name),
                'dynamodb table {} - consumed write capacity above or equal {} units ({}-{})'.format(dynamodb_tablename,
                                                                                                     consumedwritecapacityunits_threshold,
                                                                                                     region,
                                                                                                     account_name),
                'dynamodb table {} - consumed read capacity above or equal {} units ({}-{})'.format(dynamodb_tablename,
                                                                                                    consumedreadcapacityunits_threshold,
                                                                                                    region,
                                                                                                    account_name)],
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
    print('DynamoDB Tables alarms Deleted For TableName:', lb_names)


def createCloudwatchKinesis():
    for kinesis_streamName in kinesis_streamNames:
        cloudwatch.put_metric_alarm(
            AlarmName='Kinesis - {} - ReadProvisionedThroughputExceeded above or equal {} ({}-{})'.format(
                kinesis_streamName, kinesis_ReadProvision_threshold, region, account_name),
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
            AlarmName='Kinesis - {} - WriteProvisionedThroughputExceeded above or equal {} ({}-{})'.format(
                kinesis_streamName, kinesis_WriteProvision_threshold, region, account_name),
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
            AlarmName='Lambda - {} - Errors above {} Count ({}-{})'.format(
                lambda_functionName, lambda_errors_threshold, region, account_name),
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
            AlarmDescription='Alerts when Lambda {} Errors above {} Count'.format(
                lambda_functionName, lambda_errors_threshold),
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
            AlarmName='Lambda - {} - Throttles above {} Count ({}-{})'.format(
                lambda_functionName, lambda_throttles_threshold, region, account_name),
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
            AlarmDescription='Alerts when Lambda {} Throttles above {} Count'.format(
                lambda_functionName, lambda_throttles_threshold),
            TreatMissingData=lambda_throttles_TreatMissingData,
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
                'Lambda - {} - Errors above {} Count ({}-{})'.format(lambda_functionName, lambda_errors_threshold,
                                                                     region, account_name),
                'Lambda - {} - Throttles above {} Count ({}-{})'.format(lambda_functionName, lambda_throttles_threshold,
                                                                        region, account_name)],
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
    print("     [0] Exit the script.")


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