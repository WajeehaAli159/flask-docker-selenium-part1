pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build and Run Containers') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose build'
                sh 'docker-compose up -d'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'sleep 15'
                sh 'docker exec flask-docker-selenium-ci_users_1 pytest selenium_tests/'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}

