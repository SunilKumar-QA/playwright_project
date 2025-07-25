pipeline {
    agent any

    tools {
        'jenkins.plugins.shiningpanda.tools.PythonInstallation' 'Python313'
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
                bat 'python -m pip install --upgrade pip'
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
                bat 'pytest tests/ --maxfail=1 --disable-warnings -v'
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
