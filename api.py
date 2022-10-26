import boto3
from environs import Env

# Enviroment Variables
env = Env()
env.read_env()

ACCESS_KEY_ID = env.str('access_key')
ACCESS_SECRET_KEY = env.str('access_secret')
BUCKET_NAME = env.str('bucket_name')


class S3Client:
    def __init__(self):
        session = boto3.session.Session()
        self.client = session.client('s3',
                                     aws_access_key_id=ACCESS_KEY_ID,
                                     aws_secret_access_key=ACCESS_SECRET_KEY)
        self.bucket = BUCKET_NAME

    def generate_pre_signed_url(self, key, expires_in, fields=None, conditions=None):
        return self.client.generate_presigned_post(Bucket=self.bucket,
                                                   Key=key,
                                                   Fields=fields or {},
                                                   Conditions=conditions or [],
                                                   ExpiresIn=expires_in)

    def put_bucket_policy(self, policy_string):
        return self.client.put_bucket_policy(
            Bucket=self.bucket,
            Policy=policy_string
        )

    def upload_file(self, key, filename=None):
        self.client.upload_file(Bucket=self.bucket, Key=key, Filename=filename)

    def upload_file_obj(self, key, file_rb):
        self.client.upload_fileobj(Fileobj=file_rb, Bucket=self.bucket, Key=key)

    def download_file(self, key, filename):
        self.client.download_file(Bucket=self.bucket, Key=key, Filename=filename)

    def delete_file(self, key):
        self.client.delete_object(Bucket=self.bucket, Key=key)
