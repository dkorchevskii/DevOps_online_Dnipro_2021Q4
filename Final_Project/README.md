# DevOps_online_Dnipro_2021Q4

##  My final project files

### My Jenkinsfile

```
pipeline {
		//specify the desired agent
    	//agent { label 'jenkins-ec2-plugin-agent' }
		agent { label 'MainPowerAgent' }

    	stages {

        	stage('Download from git') { 
            	steps {
                	// checkout code from repo
                	checkout scm
					// list files
					sh 'ls -la'
            		}
        	}

		 	stage("testing stage") {
              	steps {
                	dir ('spring-petclinic') {
                		//run tests
                	   sh 'sh mvnw test'

               	 	}
             	 }
			}
			stage("building stage") {
				steps {
					//Dir for build
					dir ('spring-petclinic') {
						//compile project without tests
					   	sh 'sh mvnw package -DskipTests'
				}
					dir ('.') {
					 	//copy artefact to docker folder
					   	sh 'cp spring-petclinic/target/*.jar docker/petclinic.jar'
					}
				}
			}
				
			stage('Push image to registry') {
				//define variables for docker 
				environment {
					IMAGE_BASE = 'korchevskii/pet-clinic'
					IMAGE_TAG = "v$BUILD_NUMBER"
					IMAGE_NAME = "${env.IMAGE_BASE}:${env.IMAGE_TAG}"
					IMAGE_NAME_LATEST = "${env.IMAGE_BASE}:latest"
					DOCKERFILE_NAME = "docker/Dockerfile"
    			}
                steps {
               		script {
                  		//build image
                  		def dockerImage = docker.build("${IMAGE_NAME}", "-f ${DOCKERFILE_NAME} .")
						//push image to dockerhub  
						docker.withRegistry('', '4720ee8b-7f3b-4d14-b157-b63fe547ee52') {
							dockerImage.push()
                    		dockerImage.push("latest")
                  		}
                  			echo "Docker Image Pushed : ${IMAGE_NAME}"

                	}
        	  	}
     		}

			stage('Provision with terraform and deploy') {
				//credentials for terraform
				environment {
					AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
					AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
					TOKEN = credentials('telegram_bot_token')
					CHAT_ID = credentials('telegram_chat_id')
					DEV_SERVER_IP = ''
					PROD_SERVER_IP = ''
				}	
					
                steps {
					script{
						//go to terraform root folder
						dir ('terraform') {
							// infrastructure initialisation, delete previous if exist
							sh 'terraform destroy --auto-approve'
							sh "terraform init"
							sh "terraform apply --auto-approve"
							//write ip adresses to variables for notifications
							DEV_SERVER_IP = sh(returnStdout: true, script: 'terraform output -raw dev_app_server_ip').trim()
							PROD_SERVER_IP = sh(returnStdout: true, script: 'terraform output -raw prod_app_server_ip').trim()						
						}
					}
					//send ip adresses to telegram
					echo "$DEV_SERVER_IP"
					sh "curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*Job name - * *${env.JOB_NAME}*, *Build number - * *${BUILD_NUMBER}*, *Testing server address - * *http://${DEV_SERVER_IP}:80*'"
					sh "curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*Job name - * *${env.JOB_NAME}*, *Build number - * *${BUILD_NUMBER}*, *Prod server address - * *http://${PROD_SERVER_IP}:80*'"
				}	
			


			}	
			
        }    
}	



```
