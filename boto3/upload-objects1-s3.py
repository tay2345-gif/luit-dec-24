import boto3

s3=boto3.client('s3')

s3.upload_file('text_file.txt', 'tashuan-boto3-12-30-24', 'text_file_upload.txt', ExtraArgs={'ContentType':'text/plain'})