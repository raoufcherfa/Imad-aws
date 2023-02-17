<<<<<<< HEAD
# Jenkinsfil
pipeline {
    agent any

    stages {
       stage('clone github repo') {
                steps {
                    sh 'git clone https://github.com/raoufcherfa/employe.git'
                }
            }
=======
pipeline {
    agent any
    environment {
        FLASK_APP = "mp.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/raoufcherfa/employe.git']]])
            }
        }
>>>>>>> bb24e96a4098943d436dce691bbb6cb22ce8d292
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
<<<<<<< HEAD
                sh 'pytest tests/'
            }
        }
    }
}
=======
                sh 'pytest unit_tests.py'
            }
        }
        stage('Run API') {
            steps {
                sh 'python mp.py &'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout Dev && git merge origin/master'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'echo "http://localhost:5000"'
            }
        }
    }
}
>>>>>>> bb24e96a4098943d436dce691bbb6cb22ce8d292
