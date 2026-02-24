pipeline {
    agent any

    stages {

        stage('GitHub Access') {
            steps {
                echo 'Repository Cloned Successfully'
            }
        }

        stage('Environment Setup') {
            steps {
                dir('exp2') {
                    sh 'python3 --version'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Training Stage') {
            steps {
                dir('exp2') {
                    echo 'Starting Model Training...'
                    sh 'python3 train.py'
                }
            }
        }
    }
}
