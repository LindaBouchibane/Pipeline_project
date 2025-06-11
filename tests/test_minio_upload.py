import os
from utils.minio_utils import s3
from dotenv import load_dotenv

load_dotenv()

def test_minio_upload():
    BUCKET = os.getenv("MINIO_BUCKET", "pipeline-data")
    try:
        s3.head_object(Bucket=BUCKET, Key='raw/raw_data.csv')
        s3.head_object(Bucket=BUCKET, Key='processed/clean_credit_data.csv')
        print("✅ Les fichiers ont bien été uploadés dans MinIO.")
    except Exception as e:
        print("❌ Erreur : Fichier(s) manquant(s) dans MinIO.")
        print(e)
        exit(1)

if __name__ == "__main__":
    test_minio_upload()