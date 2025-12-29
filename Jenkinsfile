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
            emailext(
                subject: "Jenkins Build: ${currentBuild.currentResult}",
                body: """
                    <h2>Build Status: ${currentBuild.currentResult}</h2>
                    <p>Job Name: ${env.JOB_NAME}</p>
                    <p>Build Number: ${env.BUILD_NUMBER}</p>
                    <p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                mimeType: 'text/html',
                to: "qasimalik@gmail.com"
            )
        }
    }
}

