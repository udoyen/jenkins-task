pipeline {
    agent none
    environment {
        dockerInfo = 'dockerhub'
        githubInfo = 'github-token'
    }
    stages {
        stage {
            node {
                    checkout scm
                    myapp = docker.build("udoyen/hello-jenkins:${env.BUILD_ID}")
                    myapp.push("latest")
                    myapp.push("${env.BUILD_ID}")
            }

        }

    }
}