from utils.minio_utils import upload_file_to_minio, create_bucket_if_not_exists
from dotenv import load_dotenv
import os

load_dotenv()

BUCKET = os.getenv('MINIO_BUCKET')
create_bucket_if_not_exists(BUCKET)

# Upload fichiers après extraction et transformation
upload_file_to_minio('./data/raw/raw_data.csv', BUCKET, 'raw/raw_data.csv')
upload_file_to_minio('./data/processed/clean_credit_data.csv', BUCKET, 'processed/clean_credit_data.csv')