import boto3

s3 =boto3.client('s3')

s3.download_file('tashuan-boto3-12-30-24', 'text_file_upload.txt', 'text_file_upload.txt')
