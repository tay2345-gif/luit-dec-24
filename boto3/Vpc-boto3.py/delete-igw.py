import boto3

ec2= boto3.client('ec2')

igwid="igw-051a1f5c802d5aee4"

del_igw = ec2.delete_internet_gateway(
    InternetGatewayId=igwid,
)

print(igwid)