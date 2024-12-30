import boto3

s3 = boto3.client('s3')
# To search any partilcular folder use Prefix="folder name"
response = s3.list_objects_v2(Bucket="tashuan-boto3-12-30-24")

for content in response["Contents"]:
    if(".txt" in content["Key"]):
        print(content["Key"])