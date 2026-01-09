

pipeline{
    agent any
    stages{
        stage('checkout code'){
            steps{
                checkout scm
            }
        }
        stage('run extarct.py'){
            steps{
                bat 'Python extract.py'
            }
        }
    }
}