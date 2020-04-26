pipeline {
    agent any
    environment {
        dockerInfo = 'dockerhub'
        githubInfo = 'github-token'
    }
    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }
        stage("Build image") {
            agent {
                docker { image 'ubuntu:bionic'}
            }
            steps {
                script {
                    myapp = docker.build("udoyen/hello-jenkins:${env.BUILD_ID}")
                }
            }
        }
        stage("Push image") {
            agent {
                docker { image 'ubuntu:bionic'}
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', dockerInfo) {
                            myapp.push("latest")
                            myapp.push("${env.BUILD_ID}")
                    }
                    
                }
            }     
        }   
        stage('Deploy to kubernetes') {
            steps{
                sh "sed -i 's/hello-jenkins:latest/hello-jenkins:${env.BUILD_ID}/g' deployment.yaml"
            }
        }
        
    }    
}