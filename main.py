from api import S3Client


client = S3Client()

# client.upload_file(key='discord.png', filename='/home/bekzod/Pictures/DiscordBotThumb.png')
# print("Successfully uploaded")

# with open(file="/home/bekzod/Documents/topshiriq.docx", mode="rb") as file:
#     client.upload_file_obj(key="shop/products", file_rb=file)
# print("Successfully")

# client.download_file(key="shop/products", filename='/home/bekzod/topshiriq.docx')
# print('Downloaded successfully')

# client.delete_file(key='discord.png')
# print('Deleted successfully')

pre_signed_url = client.generate_pre_signed_url(key='shop/products', expires_in=3600)
print(pre_signed_url)