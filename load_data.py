import os
from google.cloud import storage
from dotenv import load_dotenv

def upload_file_to_storage():
    try:
        load_dotenv()
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        client = storage.Client()

        bucket_name = os.getenv('BUCKET_NAME')
        local_file_path = 'BTCUSD_1h.csv'

        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob('BTCUSD_1h.csv')
        blob.upload_from_filename(local_file_path)
        
        print("File uploaded successfully")

    except Exception as e:
        print("File upload error:", str(e))

upload_file_to_storage()