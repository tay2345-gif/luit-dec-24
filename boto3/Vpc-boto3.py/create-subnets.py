import boto3

cidrblock = "12.0.0.0/24"
vpc_id = "vpc-0c7aab619b1f088c3"

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet( CidrBlock= cidrblock, VpcId= vpc_id,)

print(subnet["Subnet"]["SubnetId"])
