pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/<your-repo>.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install -r requirements.txt
                pip install dvc[s3]
                '''
            }
        }

        stage('DVC Pull') {
            steps {
                sh 'dvc pull'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python src/train.py'
            }
        }

        stage('Show Metrics') {
            steps {
                sh '''
                echo "==== Metrics Output ===="
                cat metrics/metrics.json
                '''
            }
        }
    }
}