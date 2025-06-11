pipeline {
    agent any

    environment {
        MINIO_ENDPOINT = 'localhost:9000'
        MINIO_ACCESS_KEY = 'minioadmin'
        MINIO_SECRET_KEY = 'minioadmin'
        MINIO_BUCKET = 'pipeline-data'
        VENV = '.venv'
    }

    stages {
        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install --upgrade pip'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run ETL Pipeline') {
            steps {
                sh '.venv/bin/python3 extract/download_data.py'
                sh '.venv/bin/python3 process/transform_data.py'
                sh '.venv/bin/python3 dags/etl_pipeline.py'
            }
        }

        stage('Test MinIO Upload') {
            steps {
                sh '.venv/bin/python3 tests/test_minio_upload.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
    }
}