pipeline {
    agent any


    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                    pytest --html=Optima_Automation/reports/report.html --self-contained-html -vs
                    pwd
                    ls -l Optima_Automation/reports/
                '''
            }
        }
        stage('Post ') {

            agent{
                docker{
                    image 'amazon/aws-cli:latest'
                    args "--entrypoint=''"
                }
            }
            
            steps {

                withCredentials([usernamePassword(credentialsId: 'awsID', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        sh '''
                                aws --version
                                aws s3 ls
                                pwd
                                aws s3 cp /var/jenkins_home/workspace/git_docker/Optima_Automation/reports/report.html s3://jenkins-test-26022026/report.html
                        '''
                    }
                
            }
        }
    }
}