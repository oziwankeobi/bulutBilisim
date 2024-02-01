pipeline {
    agent any

    environment {
        URL_AWS = '891377282272.dkr.ecr.us-east-1.amazonaws.com'
        IMAGE = 'awscontainer'
        VERSION = 'latest'
    }

    stages {
        stage('Image Olusturma') {
            steps {
                script {
                    bat 'docker build -t oziwankenobi/%IMAGE% .'
                }
            }
        }
		
		stage ('DockerHub Yukleme'){
			steps {
				script {
					bat 'docker push oziwankenobi/%IMAGE%'
				}
			}
		}

        stage('AWS Yukleme ') {
            steps {
                script {
                    withAWS(credentials: 'aws-login', region: 'us-east-1') {
                        bat 'aws ecr get-login-password | docker login --username AWS --password-stdin %URL_AWS%'
                        bat 'docker VERSION %IMAGE%:%VERSION% %URL_AWS%/%IMAGE%:%VERSION%'
                        bat 'docker push %URL_AWS%/%IMAGE%:%VERSION%'
                    }
                }
            }
        }

        stage('Kubernetes Olusturma') {
            steps {
                script {
					withCredentials([file(credentialsId: 'conffile', variable: 'KUBECONFIG')]) {
						bat 'kubectl set image deployment/awsdeployment awsodev=%URL_AWS%/%IMAGE%:%VERSION%'
					}
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'docker rmi %IMAGE%'
            }
        }
    }
}
