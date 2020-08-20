pipeline {
    environment {
        registry = "docker_hub_account/repository_name"
        registryCredential = 'dockerhub'
    }
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Building docker Image') {
            steps {
                echo 'Building'
                script {
                    def customImage = docker.build("my-hello-world-image:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying docker image to registry'
               script {
                    docker.withRegistry( '', registryCredential ) {
                      customImage.push()
                    }
                  }
            }
        }
    }
}