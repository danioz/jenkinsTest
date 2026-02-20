pipeline {
    agent {
        docker { image 'python:3.12-slim' }  // Or 'python:3.11-slim' if needed
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'  // 'pip' is sufficient inside Python container
            }
        }
        stage('Run API Tests') {
            steps {
                sh 'pytest tests/ --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ])
        }
    }
}