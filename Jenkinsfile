pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Application...'
                sh 'docker build -t ayushi/sample-app:v1 .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'docker images'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Container...'
                sh 'docker run -d -p 8081:80 --name sample-app-container ayushi/sample-app:v1'
            }
        }
    }
}
