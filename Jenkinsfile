pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run ETL Pipeline') {
            steps {
                sh 'docker-compose run --rm app python extract/download_data.py'
                sh 'docker-compose run --rm app python transform/clean_transform.py'
                sh 'docker-compose run --rm app pytest tests/test_pipeline.py'
                sh 'docker-compose run --rm app python load/load_to_postgres.py'
                sh 'docker-compose run --rm app python load/load_to_mysql.py'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline terminé avec succès.'
        }
        failure {
            echo '❌ Pipeline échoué.'
        }
    }
}
