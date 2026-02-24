pipeline {
    agent any
    environment {
        HOME = '/tmp'
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('pytest') {
            agent{
                docker {
                    image 'python'
                    image 'selenium/standalone-chrome:latest'
                    reuseNode true
                }

            }
            steps {
                sh '''
                    python --version
                    pwd
                    python -m venv venv
                    . venv/bin/activate
                    pwd
                    pip install -r requirements.txt
                    pytest Optima_Automation -vs
                '''

            }
        }
    }

}
