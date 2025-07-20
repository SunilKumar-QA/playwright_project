pipeline {
    agent any

    environment {
        // Optional: Use a virtual environment if needed
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout Code') {
            steps {
                // This checks out your code from Git
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                // Make sure Python and pip are available
                sh 'python --version'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                // Install Playwright browsers
                sh 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Playwright tests with Pytest
                sh 'pytest tests/ --headed --maxfail=1 --disable-warnings -v'
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