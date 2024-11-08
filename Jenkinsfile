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
                    // Оновлюємо pip
                    sh 'pip install --upgrade pip --break-system-packages'
                    // Встановлюємо залежності з requirements.txt
                    sh 'pip install -r requirements.txt --break-system-packages'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Переконайтеся, що віртуальне середовище активоване, і додаємо шлях до pytest у PATH
                    sh 'export PATH=$PATH:/var/lib/jenkins/.local/bin'
                    // Запускаємо тести
                    sh './venv/bin/pytest --disable-warnings'
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


