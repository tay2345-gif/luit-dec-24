import boto3

ec2 =boto3.client("ec2")

rtb_id ="rtb-0d45cf1e2aaf90c96"
subnet_id = "subnet-09e1dc8c531fed379"

subnetassoc = ec2.associate_route_table (RouteTableId= rtb_id, SubnetId= subnet_id)

print(subnetassoc["AssociationId"])