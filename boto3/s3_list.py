import boto3
# Lets use Amazon S3 bucket
s3 = boto3.resource('s3')
# List all buckets in this account
count = 0
for bucket in s3.buckets.all():
    print(bucket.name)
    count = count + 1
# Print the total number of buckets
print("Total bucket count is:", count)
