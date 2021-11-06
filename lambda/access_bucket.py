import boto3
from credentials import *


def access_s3_bucket():

    bucket = 'newyorker'
    file = 'records.json'

    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    return s3.Object(bucket, file)
