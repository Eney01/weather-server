pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Eney01/weather-server.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Створення віртуального середовища
                    sh 'python3 -m venv venv'
                    // Активуємо віртуальне середовище
                    sh '. venv/bin/activate'
                    // Переконуємось, що pip є оновленим
                    sh 'pip install --upgrade pip'
                    // Встановлення залежностей
                    sh 'pip install -r requirements.txt --break-system-packages'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестів
                    sh './venv/bin/pytest --disable-warnings'
                }
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

