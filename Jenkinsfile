pipeline {
    agent any
    
    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Eney01/weather-server.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Створюємо віртуальне середовище
                    sh 'python3 -m venv $VENV_DIR'
                    // Активуємо віртуальне середовище
                    sh '. $VENV_DIR/bin/activate'
                    // Встановлюємо залежності
                    sh '$VENV_DIR/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запускаємо тести в активованому середовищі
                    sh '$VENV_DIR/bin/pytest --disable-warnings'
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
