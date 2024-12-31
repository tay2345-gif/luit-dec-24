import boto3 

vpc_id = 'vpc-0c7aab619b1f088c3'

ec2 = boto3.client('ec2')

rtb = ec2.create_route_table(VpcId= vpc_id )

print(rtb["RouteTable"]["RouteTableId"])