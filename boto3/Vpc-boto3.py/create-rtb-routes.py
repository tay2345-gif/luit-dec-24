import boto3 

ec2 = boto3.client('ec2')

gwid = "igw-051a1f5c802d5aee4"
rtb_id = "rtb-0d45cf1e2aaf90c96"

route = ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId= gwid,
    RouteTableId= rtb_id,
)

print(route)