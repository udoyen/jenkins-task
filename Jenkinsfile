pipeline {
    
    environment {
    registry = "udoyen/hello-jenkins"
    registryCredential = 'dockerhub'
    }  
  agent any  
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          
        }
      }
    }
    stage('Deploy Image') {
        steps{    
              script {
              docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
              }
            }
        }
    }

    stage('Deploy to kubernetes') {
      steps{
        script {
          sh "sed -i 's/hello:latest/hello:${env.BUILD_NUMBER}/g' deployment.yaml"
          sh "kubectl get pods"

        }
      }
    }
  }
}