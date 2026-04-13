pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/2022BCS0025-PRANATHI/batch2_2022BCS0025.git'
            }
        }

        stage('Display Info') {
            steps {
                bat 'echo Name: Pranathi Mantri'
                bat 'echo Roll No: 2022BCS0025'
                bat 'echo Bucket: batch2-2022bcs0025'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install pandas dvc[s3]
                '''
            }
        }

        stage('DVC Pull') {
            steps {
                bat 'python -m dvc pull'
            }
        }

        stage('Train V1') {
            steps {
                bat 'python src/train.py data/dataset_v1/wine.csv'
            }
        }

        stage('Train V2') {
            steps {
                bat 'python src/train.py data/dataset_v2/wine.csv'
            }
        }

        stage('Show Metrics') {
            steps {
                bat '''
                echo ==== FINAL METRICS OUTPUT ====
                type metrics\\metrics.json
                '''
            }
        }
    }
}
