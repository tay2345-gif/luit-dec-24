import boto3

s3=boto3.client('s3')

response = s3.generate_presigned_url('get_object',Params={'Bucket': "tashuan-boto3-12-30-24",'Key': "text_file_upload.txt"}, ExpiresIn=300)

print (response)