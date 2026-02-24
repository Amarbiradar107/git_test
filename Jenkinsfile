pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Pytest in Docker') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    python --version
                    pwd
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest Optima_Automation -vs
                '''
            }
        }
    }
}