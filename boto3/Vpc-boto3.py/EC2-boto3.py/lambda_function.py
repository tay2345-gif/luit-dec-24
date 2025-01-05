import boto3 

def lambda_handler(event, context):
    import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(
    InstanceIds=[
        'i-013ec67e39aa9e355','i-0fbef8e6a2370d269','i-090fca044f92ff225'
    ],
)

print(response)
