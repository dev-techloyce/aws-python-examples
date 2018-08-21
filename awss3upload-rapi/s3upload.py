#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3upload.py
# s3upload is an example that handles S3 buckets on AWS
# It uses Resource API (high-level) of Boto3
# Upload a local file to a S3 bucket
# You must provide 1 parameter:
# BUCKET_NAME     = Name of the bucket
# OBJECT_NAME     = Object file name in the bucket
# LOCAL_FILE_NAME = Local file name

import sys
import boto3
import botocore

def main():

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if len(args) < 3:
    print('Not enough parameters. Proper Usage is: python s3upload.py <BUCKET_NAME> <OBJECT_NAME> <LOCAL_FILE_NAME>')
    sys.exit(1)

  bucket_name = args[0]
  key_name = args[1]
  upload_file_name = args[2]

  print('Bucket:     ' + bucket_name)
  print('Object/Key: ' + key_name)
  print('Local file: ' + upload_file_name)

  # Instantiate the service resource object
  s3resource = boto3.resource('s3')

  try:
    #  Instantiate the bucket object
    bucket = s3resource.Bucket(bucket_name)
    print('Uploading object...')
    # Upload object
    bucket.upload_file(upload_file_name, key_name)
    print('\nUploaded')
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "NoSuchBucket":
      print("Error: Bucket does not exist!!")
    elif e.response['Error']['Code'] == "InvalidBucketName":
      print("Error: Invalid Bucket name!!")
    elif e.response['Error']['Code'] == "AllAccessDisabled":
      print("Error: You do not have access to the Bucket!!")
    else:
      raise

  return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
