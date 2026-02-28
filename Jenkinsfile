pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('aws cli') {

            agent{
                docker{
                    image 'amazon/aws-cli:latest'
                }
            }
            
            steps {
                sh '''
                    aws --version
                '''
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t selenium-pytest .'
            }
        }

        stage('Run Pytest in Docker') {
            agent {
                docker {
                    image 'selenium-pytest'      // use the image we just built
                    args '-u root'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    python --version
                    pwd
                    pip install --upgrade pip    # requirements already in image
                    google-chrome --version || echo "chrome not installed"
                    pytest Optima_Automation -vs
                '''
            }
        }
    }
}