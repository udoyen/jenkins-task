pipeline {
    
    environment {
    registry = "udoyen/hello-jenkins"
    registryCredential = 'dockerhub'
    dockerImageUsed = 'benhall/dind-jenkins-agent:v2'
    }  
  agent any
  stages {
    stage('Building image') {
      container('jnlp') {
        steps{
          script {
            dockerImage = docker.build registry + ":$BUILD_NUMBER"
            
          }
        }
      }
    }
    stage('Deploy Image') {
        container('jnlp') {
          steps{    
                script {
                docker.withRegistry( '', registryCredential ) {
                  dockerImage.push()
                }
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