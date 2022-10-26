from api import S3Client


client = S3Client()

# client.upload_file(key='discord.png', filename='/home/bekzod/Pictures/DiscordBotThumb.png')
# print("Successfully uploaded")
with open(file="/home/bekzod/Documents/topshiriq.docx", mode="rb") as file:
    client.upload_file_obj(key="shop/products", file_rb=file)
print("Successfully")

# client.delete_file(key='discord.png')
# print('Deleted successfully')
