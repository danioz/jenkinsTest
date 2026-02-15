pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to staging...'
            }
        }
    }
}