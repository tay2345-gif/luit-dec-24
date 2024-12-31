import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for rtb in response["RouteTables"]:
    print (rtb ["VpcId"],  rtb["RouteTableId"])

    for association in rtb ["Associations"]:
        print (association["RouteTableAssociationId"])
        if "SubnetId" in association:
            print(association["SubnetId"])

for routes in rtb["Routes"]:
    print (routes ["DestinationCidrBlock"], routes["GatewayId"])