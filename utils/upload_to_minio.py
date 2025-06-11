import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.minio_utils import s3
import os

def test_minio_upload():
    bucket = os.getenv("MINIO_BUCKET", "data-pipeline")
    try:
        s3.head_object(Bucket=bucket, Key="raw/raw_data.csv")
        s3.head_object(Bucket=bucket, Key="processed/clean_credit_data.csv")
        print("✅ Fichiers trouvés dans MinIO.")
    except Exception as e:
        print("❌ Erreur :", e)
        assert False, "Fichiers manquants dans MinIO"