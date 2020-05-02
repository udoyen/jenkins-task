podTemplate(label: 'mypod', containers: [
    containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
    containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl', command: 'cat', ttyEnabled: true)
  ],
  volumes: [
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
  ]
  ) {
    registry = "udoyen/hello-jenkins"
    registryCredential = 'dockerhub'
    dockerImage = ''
    node('mypod') {
        stage('Check running containers') {
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

	stage('kubernetes Deployment') {
           
            container('kubectl') {
                 sh "sed -i 's/image:\s*udoyen\/hello-jenkins/image: udoyen\/hello-jenkins:${BUILD_NUMBER}/g' ${WORKSPACE}/deployment.yaml"
                 sh "kubectl apply -f ${WORKSPACE}/deployment.yaml"
                 sh "kubectl apply -f ex.yaml"
          
            }

        }
        
    }
  }