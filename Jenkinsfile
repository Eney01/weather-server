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
                    // Активуємо віртуальне середовище та оновлюємо pip всередині нього
                    sh '. venv/bin/activate && ./venv/bin/pip install --upgrade pip'
                    // Встановлюємо залежності в віртуальному середовищі
                    sh '. venv/bin/activate && ./venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запускаємо тести у віртуальному середовищі
                    sh '. venv/bin/activate && ./venv/bin/pytest --disable-warnings'
                }
            }
        }
    }

    post {
        always {
            // Архівуємо результати тестів
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
