<<<<<<< HEAD
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/amsolaces/SymbiosisForm.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myapp .'
            }
        }

        stage('Run Test') {
            steps {
                bat 'docker run myapp'
            }
        }
    }
=======
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/amsolaces/SymbiosisForm.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myapp .'
            }
        }

        stage('Run Test') {
            steps {
                bat 'docker run myapp'
            }
        }
    }
>>>>>>> a6d49f4f9bf51254ed48dc53d613efb206796e34
}