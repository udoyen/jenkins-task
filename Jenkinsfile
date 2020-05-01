pipeline {
    
    environment {
    registry = "udoyen/hello-jenkins"
    registryCredential = 'dockerhub'
    }  
  agent none 
  stages {
    stage('Building image') {
      agent {
          label 'docker-agent'
      }
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          
        }
      }
    }
    stage('Deploy Image') {
        agent {
          label 'docker-agent'
        }
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
          sh '''
              eval $(minikube docker-env);
              kubectl get services;

            '''

        }
      }
    }
  }
}