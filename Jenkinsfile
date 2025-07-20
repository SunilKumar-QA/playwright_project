pipeline {
    agent any

    tools {
        // This uses Pyenv Pipeline Plugin
        pyenv '3.11.8'  // Must match the version installed via pyenv
    }
    

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                bat 'python --version'
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/ --headed --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo '❌ Tests failed!'
        }
        success {
            echo '✅ Tests passed!'
        }
    }
}