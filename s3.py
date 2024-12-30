import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='tashuan-boto3-12-30-24'
)

print (response)