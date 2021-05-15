# To Run Script
# Run: python ec2_disable_detail_monitoring.py


# Import required libraries. If these are not already installed on the client they will need to be installed first with pip or other package manager
import os
import boto3
import sys


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
# cloudwatch = boto3.client('cloudwatch', region_name=region)

# Get an EC2 client object
ec2 = boto3.client('ec2', region_name=region)

# Get all the Instances in the account
ec2Instances = ec2.describe_instances()


# ================================================================================================================
# EC2 Detail Monitoring Functions (Do not touch!)
# ================================================================================================================

# Iterate through the Instances
def listEC2():
    for r in ec2Instances['Reservations']:
        for i in r['Instances']:

            # Get the InstanceId
            thisInstanceId = i['InstanceId']

            # Get the current Instance Monitor setting
            thisInstanceMonitoringEnabled = i['Monitoring']['State']

            # Function to grab EC2 Name tag
            def ec2Tags():
                tags = boto3.client('ec2', region_name=region)
                response = tags.describe_tags(
                    Filters=[
                        {
                            'Name': 'resource-id',
                            'Values': [
                                ''.join(thisInstanceId)
                            ]
                        },
                    ]
                )
                for tag in response['Tags']:
                    if tag['Key'] == 'Name':
                        return tag['Value']

            # Check if detailed monitoring is already enabled
            if thisInstanceMonitoringEnabled == "enabled":
                print("Detailed monitoring is enabled on " + ec2Tags() + ' | ' + thisInstanceId)
                break
            # else:
            #     print("All EC2 detailed monitoring has already been disabled")


# Iterate through the Instances
def listEC2andDisable():
    for r in ec2Instances['Reservations']:
        for i in r['Instances']:

            # Get the InstanceId
            thisInstanceId = i['InstanceId']

            # Get the current Instance Monitor setting
            thisInstanceMonitoringEnabled = i['Monitoring']['State']

            # Function to grab EC2 Name tag
            def ec2Tags():
                tags = boto3.client('ec2', region_name=region)
                response = tags.describe_tags(
                    Filters=[
                        {
                            'Name': 'resource-id',
                            'Values': [
                                ''.join(thisInstanceId)
                            ]
                        },
                    ]
                )
                for tag in response['Tags']:
                    if tag['Key'] == 'Name':
                        return tag['Value']

            # Check if detailed monitoring is already enabled
            if thisInstanceMonitoringEnabled == "enabled":

                # Disable the monitoring
                result = ec2.unmonitor_instances(InstanceIds=[thisInstanceId])

                # Check if the API call succeeded
                if result['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print("Detailed monitoring disabled on " + ec2Tags() + ' | ' + thisInstanceId)
                else:
                    print("Error disabling detailed monitoring on " + ec2Tags() + ' | ' + thisInstanceId)
                    print(result)

            # Skip the instance if monitoring was already disabled
            else:
                print("Skipping " + ec2Tags() + ' | ' + thisInstanceId + " as detailed monitoring is already disabled")


# ================================================================================================================
# Main Function (Do not touch!)
# ================================================================================================================


def menu():
    print()
    print("EC2 Detailed Monitoring Script")
    print()
    print("     [1] List EC2 that only have detailed monitoring enabled.")
    print("     [2] List EC2 w/ detailed monitoring and disable all.")
    print("     [3] Restart Script. Deletes Variables from Memory.")
    print("     [0] Exit the script")


def main():
    menu()
    print()
    option = int(input("Enter your option: "))
    print()

    while option != 0:
        if option == 1:
            listEC2()
            input("Press Enter to continue...")
        elif option == 2:
            listEC2andDisable()
            input("Press Enter to continue...")
        elif option == 3:
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
