pipeline {
    agent any

    environment {
        IMAGE_NAME     = "flask-app:latest"
        CONTAINER_NAME = "flask-app"
        APP_PORT       = "7000"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out from GitHub..."
                git branch: 'trunk', url: 'https://github.com/Anji392/myrepo.git'
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
                    if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
                        echo "Old container found. Removing..."
                        docker rm -f ${CONTAINER_NAME} || true
                    else
                        echo "No existing container to stop."
                    fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo "Running new container..."
                sh '''
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}
                    sleep 5
                '''
            }
        }

      stage('Health Check') {
    steps {
        echo "Performing health check on Flask app..."
        sh '''
            echo "Containers running:"
            docker ps

            echo "Health check against flask-app container..."
            curl -f http://flask-app:${APP_PORT}/ || (echo "Health check failed" && exit 1)
        '''
        echo "🚀 Flask app is successfully deployed on port ${APP_PORT}"
    }
}

