import boto3

s3 = boto3.client('s3')

with open ("text_file.txt", 'rb') as f:
   s3.put_object(Bucket="tashuan-boto3-12-30-24", Key="text_file.txt", Body=f, ContentType="text/plain")

