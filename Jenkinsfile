pipeline {
  agent {
    kubernetes {
      yaml ''' 
apiVersion: v1
kind: Pod
spec:
   containers:
   - name: docker
     image: docker:1.11
     command: [\'cat\']
     tty: true
     volumeMounts:
     - name: dockersock
       mountPath: /var/run/docker.sock
   volumes:
   - name: dockersock
     hostPath:
       path: /var/run/docker.sock
'''
		}
	}
   agent {
         kubernetes {
      yaml '''
      apiVersion: v1
      kind: Pod
      spec:
         containers:
         - name: kubectl
         image: lachlanevenson/k8s-kubectl:v1.8.8
         command: ['cat']
         tty: true
      '''
    }
      }
  stages {
    stage('Build and deploy') {
      steps {
        git 'https://github.com/udoyen/jenkins-task.git'
        container(name: 'docker') {
          script {
            dockerImage = docker.build registry + ":$BUILD_NUMBER"
            docker.withRegistry( '', registryCredential ) {
              dockerImage.push()
            }
          }
        }
       
      }

    }

    stage {
      stage('Deploy To Kubernetes') {
        steps {
          container('kubctl') {
            sh 'kubectl get pods'
          }
       }
     }
   }

  }
    
  environment {
    registry = 'udoyen/hello-jenkins'
    registryCredential = 'dockerhub'
    dockerImage = ''
      }
}