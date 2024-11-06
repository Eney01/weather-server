pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Вказуємо правильну гілку та URL репозиторію
                git branch: 'main', url: 'https://github.com/Eney01/weather-server.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --disable-warnings'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/test-results/*.xml', allowEmptyArchive: true
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}

