pipeline {
  environment {
     registry = "udoyen/hello-jenkins"
     registryCredential = 'dockerhub'
     dockerImage = ''
    }
  agent {
	kubernetes {
yaml ''' 
apiVersion: v1
kind: Pod
spec:
   containers:
   - name: docker
     image: docker:1.11
     command: ['cat']
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

   stages {

	stage('Build and deploy') {
		steps {
		    git 'https://github.com/udoyen/jenkins-task.git'
            container('docker') {
                // example to show you can run docker commands when you mount the socket
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
		  }
	}

 }

}
	