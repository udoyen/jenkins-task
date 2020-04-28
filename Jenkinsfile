pipeline {
    agent {
        label 'docker-agent'
    }
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
        stage("Build image and push") {
            agent {
                docker {
                label 'docker-agent'
                image 'udoyen/dind-jenkins-agent:v2'               

                }
            }
            steps {
                script {
                    //myapp = sh "/usr/bin/docker build -t udoyen/hello-jenkins:${env.BUILD_ID}"
                    myapp = docker.build("udoyen/hello-jenkins:${env.BUILD_ID}")
                    myapp.push("latest")
                    myapp.push("${env.BUILD_ID}")
                }
            }
        }
        
    }    
}