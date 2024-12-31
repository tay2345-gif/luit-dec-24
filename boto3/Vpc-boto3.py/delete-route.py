import boto3

ec2 = boto3.client("ec2")

rtb_id ="rtb-0d45cf1e2aaf90c96"

Del_route = ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId= rtb_id,
)

print(Del_route)