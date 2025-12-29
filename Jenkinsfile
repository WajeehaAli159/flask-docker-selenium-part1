pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/WajeehaAli159/flask-docker-selenium-part1.git'
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
                sh '''
                sleep 15
                docker exec flask-tdd-testdrivenio_users_1 pytest selenium_tests/
                '''
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}

