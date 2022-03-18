import boto3
# import datetime
from datetime import datetime
# strftime("%H:%M:%S")
now  = datetime.now().strftime("%d")
# List all regions
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
print(regions)

for region in regions:
    ec2_client = boto3.client('ec2',region_name=region)

    running_instances = ec2_client.describe_instances()
    for reservation in running_instances['Reservations']:
        for instance in reservation['Instances']:
            print("%s %s" % (instance['InstanceId'], instance['LaunchTime']))
            instance_id = instance['InstanceId']
            instance_launchtime = instance['LaunchTime'].strftime("%d")
            # print(datetime.now())
            days_diff = int(now)-int(instance_launchtime)
            print(int(now)-int(instance_launchtime))
            if days_diff >=1:
                print("kill   ", instance_id)
            else:
                print("let live")










# # response = client.describe_instances()
# # print(response)

# for region in regions:
#     conn = boto3.resource('ec2',region_name=region)
#     instances = conn.instances.filter()
#     count = 0
#     for instance in instances:
#         # print(instance)
#         if instance.state["Name"] == "running":
#             count+=1
#             print("running instance No: ", count)
#             print (instance.id, instance.instance_type,instance.tags,instance.launch_time, region)
            # print(instance.)
# # ec2 = boto3.client('ec2')
# # response = ec2.describe_instances()
# # print(response)

# import boto.ec2

# conn = boto.ec2.connect_to_region('ap-south-1')
# reservations = conn.get_all_instances()
# for r in reservations:
#     for i in r.instances:
#         print('%s\t%s' % (i.id, i.launch_time))


