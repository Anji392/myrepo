pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app:latest"
        CONTAINER_NAME = "flask-app"
        APP_PORT = "7000"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out from GitHub..."
                // Jenkins auto-checks out the source code
                sh 'ls -l'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "Stopping old container if exists..."
                sh '''
                    if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}\$"; then
                        docker rm -f ${CONTAINER_NAME} || true
                    fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo "Running new container..."
                sh 'docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}'
            }
        }
    }

    post {
        success {
            echo "🚀 Flask app is successfully deployed on port ${APP_PORT}"
        }
        failure {
            echo "❌ Deployment failed. Check the logs!"
        }
    }
}

