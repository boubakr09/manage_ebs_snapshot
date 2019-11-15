import boto3
import datetime
from datetime import timezone


#Create an ec2 client
ec2 = boto3.client('ec2')

#The AWS account on which the ebs snapshots are(to be enter)
accountownerid = 'account_owner_id'
#The number of days before the snapshot would be deleted (by default 15)
reference_value = "15"
#get the today date and convert it in UTC
date = (datetime.datetime.today()).replace(tzinfo=timezone.utc)

#get the snapshots informations
response = ec2.describe_snapshots(
    OwnerIds=[
        accountownerid
    ]
)

#verify if there is any snapshots in the account
if (response['Snapshots']) == '[]':
    #print this message if there is no snapshots
    print ('There is no snapshot available in account: '+accountownerid)
#else, browse the list of the existing snapshots
else:
    for i in response['Snapshots']:
        #save the snapshot creation time
        creation_time = (i['StartTime'])
        #save the snapshot ID
        snapshotid = (i['SnapshotId'])
        #get the number of days between the sanpshot creatio time and the today date
        days_between = creation_time - date
        #format the number of days into string
        format_days_between = (str(days_between))
        #compare the number of days and the reference value, if the condition match, delete the snapshots
        if (format_days_between[1:2]) == reference_value or (format_days_between[1:2]) > reference_value:
            snapshot = ec2.delete_snapshot(
                SnapshotId=snapshotid
            )
        #else, print a message
        else:
            print ('No snapshot to delete')
