import json
from api import S3Client
from bucket_policy import ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER_BUCKET_POLICY


client = S3Client()

# client.upload_file(key='discord.png', filename='/home/bekzod/Pictures/DiscordBotThumb.png')
# print("Successfully uploaded")

# with open(file="/home/bekzod/Documents/topshiriq.docx", mode="rb") as file:
#     client.upload_file_obj(key="shop/products", file_rb=file)
# print("Successfully")

# client.download_file(key="test/shop/product/excel/2/products.xlsx", filename='/home/bekzod/products.xlsx')
# print('Downloaded successfully')

# Bucket Policy
# json_string = json.dumps(ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER_BUCKET_POLICY)
# client.put_bucket_policy(policy_string=json_string)
# print('Successfully')


# bucket_policy = {
#     'Version': '2012-10-17',
#     'Statement': [{
#         'Sid': 'AddPerm',
#         'Effect': 'Allow',
#         'Principal': '*',
#         'Action': ['s3:GetObject'],
#         'Resource': f'arn:aws:s3:::testbucketwithpy/*'
#     }]
# }

# Convert the policy from JSON dict to string
# bucket_policy = json.dumps(bucket_policy)
# client.put_bucket_policy(policy_string=bucket_policy)
# print('Successfully')


# Get Bucket Policy
# print(client.get_bucket_policy())

# client.delete_file(key='discord.png')
# print('Deleted successfully')

pre_signed_url = client.generate_pre_signed_url(key='test/shop/product/excel/2/products.xlsx', expires_in=3600)
print(pre_signed_url)