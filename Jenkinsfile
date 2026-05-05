pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Application...'
                sh 'docker build -t quotesops .'
'
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
                sh 'docker run -d -p 8000:8000 quotesops'
            }
        }
    }
}
