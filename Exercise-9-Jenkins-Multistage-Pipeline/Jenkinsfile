pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '.venv/bin/python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    mkdir -p "$WORKSPACE/python-app-deploy"
                    cp app.py requirements.txt "$WORKSPACE/python-app-deploy/"
                    cp -R .venv "$WORKSPACE/python-app-deploy/"
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting Flask application...'
                sh '''
                    cd "$WORKSPACE/python-app-deploy"
                    nohup .venv/bin/python app.py > app.log 2>&1 &
                    echo $! > app.pid
                    for i in $(seq 1 20); do
                        if curl -fsS http://127.0.0.1:5001/; then
                            exit 0
                        fi
                        sleep 1
                    done
                    cat app.log
                    exit 1
                '''
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing the deployed application...'
                sh '''
                    curl -fsS http://127.0.0.1:5001/
                    echo
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
