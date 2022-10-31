BUCKET_NAME = 'testbucketwithpy'
SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER = 'test/shop/product/excel'



ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER_BUCKET_POLICY = {
    "Id": "PolicyExcelFileFolder20220522",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StmtExcelFileFolderPutObject",
            "Action": [
                "s3:PutObject"
            ],
            "Effect": "Deny",
            "NotResource": [
                f"arn:aws:s3:::{BUCKET_NAME}/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*.xls",
                f"arn:aws:s3:::{BUCKET_NAME}/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*.XLS",
                f"arn:aws:s3:::{BUCKET_NAME}/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*.xlsx",
                f"arn:aws:s3:::{BUCKET_NAME}/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*.XLSX",
                f"arn:aws:s3:::{BUCKET_NAME}/test/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*",
                f"arn:aws:s3:::{BUCKET_NAME}/media/*"
            ],
            "Principal": "*",
        },
        {
            "Sid": "StmtExcelFileFolderGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
            ],
            "Resource": [
                f"arn:aws:s3:::{BUCKET_NAME}/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*",
                f"arn:aws:s3:::{BUCKET_NAME}/test/{SHOP_ALL_PRODUCTS_DATA_EXCEL_FILES_FOLDER}/*",
                f"arn:aws:s3:::{BUCKET_NAME}/media/*"
            ]
        }
    ]
}