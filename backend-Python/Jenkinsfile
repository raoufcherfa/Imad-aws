# Jenkinsfil
pipeline {
    agent any

    stages {
       stage('clone github repo') {
                steps {
                    sh 'git clone https://github.com/raoufcherfa/employe.git'
                }
            }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}