

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
                bat 'C:\\Users\\S\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py'
            }
        }
    }
}