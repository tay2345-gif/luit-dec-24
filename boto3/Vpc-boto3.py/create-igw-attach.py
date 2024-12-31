import boto3

ec2 = boto3.client("ec2")

igw_id = "igw-051a1f5c802d5aee4"
vpc_id = "vpc-0c7aab619b1f088c3"

igw_att = ec2.attach_internet_gateway(InternetGatewayId= igw_id ,VpcId=vpc_id )

print(igw_att)