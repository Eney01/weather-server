pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Клонуємо репозиторій з гілкою main
                git branch: 'main', url: 'https://github.com/Eney01/weather-server.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Встановлюємо залежності з requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Запускаємо тести з pytest
                sh 'pytest --disable-warnings'
            }
        }
    }
    
    post {
        always {
            // Архівуємо результати тестів (якщо є)
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


