import sys
import boto3

def main(bucket, aws_access_key_id, aws_secret_access_key):
    print("=========================")
    from s3os import os
    print(os)
    os.authorize(bucket, aws_access_key_id, aws_secret_access_key)
    os.listdir("/")

    from s3os import shutil
    shutil.authorize(bucket, aws_access_key_id, aws_secret_access_key)

if __name__ == "__main__":
    try:
        bucket = sys.argv[1]
        aws_access_key_id = sys.argv[2]
        aws_secret_access_key = sys.argv[3]
        main(bucket, aws_access_key_id, aws_secret_access_key)
    except Exception as err:
        print(err)