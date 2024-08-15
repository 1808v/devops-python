
#functions
def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

#print(dir(s3_obj.buckets))
#print(s3_obj.buckets.all.__doc__)
#all_buckets = print(s3_obj.buckets.all)
#print(all_buckets)

def upload_file(s3_obj,bucket_name,file_path,key_name):
    file_data = open(file_path, 'rb') #open
    s3_obj.Bucket(bucket_name).put_object(Key=key_name,Body=file_data) #processed 
    file_data.close() #closed 
    print("file uploaded succesfully")

def list_file(s3_obj,bucket_name,):
    print(f"the objects in {bucket_name} are :")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)

def create_bucket(s3_obj,bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})
    print(f"bucket {bucket_name} created succesfully")