pipeline {
    agent any

    stages {

        stage('docker build') {
            steps {
                sh 'docker build -t Selenium-pytest .'
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Pytest in Docker') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-u root' 
                    reuseNode true
                }
            }
            steps {
                sh '''
                    python --version
                    pwd
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    google-chrome --version
                    pytest Optima_Automation -vs
                '''
            }
        }
    }
}