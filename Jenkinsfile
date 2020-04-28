pipeline {
    
    environment {
    registry = "udoyen/hello-jenkins"
    registryCredential = 'dockerhub'
    }  
  agent any  
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/udoyen/jenkins-task.git'
      }
    }
    stage('Building image') {
      agent {
          docker {
              label 'docker-agent'
              image 'udoyen/dind-jenkins-agent:v2'
          }
      }
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          
        }
      }
    }
    stage('Deploy Image') {
        agent {
            docker {
                label 'docker-agent'
                image 'udoyen/dind-jenkins-agent:v2'
            }
        }
        steps{    
              script {
              docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
              }
            }
        }
    }
  }
}