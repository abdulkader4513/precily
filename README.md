### Assessment Task

Devops Engineer


#### Given: 

You are given an application with APIs which extracts text from images.


#### Task: 

You have to build a lightweight docker container which will map port 4000 of

your app to your machine. You also have to create a Kubernetes manifest file which

can deploy replica sets in a cluster. Create a requirements.txt file for this repo. Create

a contract of rest api read_ocr. The solution will be evaluated by running the manifest

file on minikube.

Note: Please download this repo and email a zip file over email.

Extra marks will be given for:

• setting up CI/CD files for the same app.

• adding logging functionality in repo.

Dependencies: opencv-python==4.4.0.46 pytesseract==0.3.7

Please find the link below:

<https://github.com/precilyinc/tess/blob/main/README.md>


### Solution

1. Cloned the provided github repo

2. Created requirements.txt in the root folder for the dependencies. Initially tried with opencv-python module but faced few issues. Upon researching, it was suggested to use opencv-python-headless instead.

   1. opencv-python-headless==4.6.0.66
   2. pytesseract==0.3.10
   3. Flask==2.2.2
   4. requests==2.28.1
   5. urllib3==1.26.13

Directory Structure so far:

precily

|\_\_\_\_ app.py

|\_\_\_\_ views.py

|\_\_\_\_ README.md

|\_\_\_\_ requirements.txt

3. Make the flask application running locally using **_python app.py_**. Tested the root  from the browser and got the expected response {"API Documentation":""}

![](https://lh6.googleusercontent.com/kUqdceGtvEyP5czIAlEjSWI2EF1dt3qAdL15hdmUebrOCAglDC_oIk7FoynoUACVCjbtTBvfrwqQz9BrFteqV4Oalz2EZLOdjY6IDFw7h5PTRl4dZtKzHNPnR6vqFr505YtHtItBC_yV_d5yvngFBUdd7BgTPpipwCk89GsORj366WCza9Rz2aQ314xSeg)

4. Created Dockerfile in the root directory. Dockerfile has the following # Dockerfile

_FROM python:3.8-slim-buster_

_WORKDIR /app_

_COPY requirements.txt requirements.txt_

_RUN pip3 install -r requirements.txt_

_COPY . ._

_EXPOSE 4000_

_CMD \["python", "app.py"]_

Used python 3.8 version and chosen slim-buster inorder to reduce the size of the docker images. This can help us deploy the docker image faster. Created a working directory. Copied only requirements.txt because docker images are built layer by layer. Whenever the bottom layer gets changed, all the layers above them are rebuilt. So, application code changes often however, dependencies won't change much. Moreover, building the dependencies takes more time during the building process. Downloading and Installation of all the required dependencies is done using the command pip3 install. Source code is copied to the container and port 4000 is exposed as per the given task. Finally ran the app.py file from the container.

Directory Structure so far:

precily

|\_\_\_\_ app.py

|\_\_\_\_ views.py

|\_\_\_\_ README.md

|\_\_\_\_ requirements.txt

|\_\_\_\_ Dockerfile

5. Build and Pushed the docker image

Created a new repository named precily in the Docker Hub account. Docker image is built using docker build command and tag is used to set the name of the image. Docker images command is used to list the images and docker push command is used to push it to the docker hub repository. 

1. _docker build --tag abdulkader4513/precily:latest ._
2. _docker images_
3. _docker push abdulkader4513/precily:latest ._

![](https://lh3.googleusercontent.com/tF9svcd3d_0VnnrYqNKPXgrGeOdQ48moJm108zA4_WbQVrE31yROVoI8DSJ5BNZQ82c0Z-1lRYBNDZTfXZobRc1ZoUKLZojDVNbagT0uDlcTxlpE6oZZa5vJ6-Zcrv_MlnYNFMxtZOx9FxV3_oYC79rsZfOi6n7L4imcsyljBTiBDTGIdwT63oG-xIV3nA)

6. Created a new github repository named precily and added all the files to the repository. Repository link: <https://github.com/abdulkader4513/precily>
7. Created an Ubuntu EC2 instance with t3.large instance size and 30 GB EBS volume disk space.
8. Connected to the EC2 instance from the browser using EC2 instance connect. 
9. Update the apt package index and installed the docker

_sudo apt-get update_

_sudo apt-get install \\_

_    ca-certificates \\_

_    curl \\_

_    gnupg \\_

_    lsb-release_

_sudo mkdir -p /etc/apt/keyrings_

_curl -fsSL https&#x3A;//download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg_

_echo \\_

_  "deb \[arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https&#x3A;//download.docker.com/linux/ubuntu \\_

_  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null_

_  _

_sudo apt-get update_

_sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin_

_sudo service docker start___

10. Installed kubectl using the below commands

_curl -LO "https&#x3A;//dl.k8s.io/release/$(curl -L -s https&#x3A;//dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"_

_sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl_

_kubectl version --client_

11. Minikube installation is done using the below commands

_curl -LO https&#x3A;//storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64_

_sudo install minikube-linux-amd64 /usr/local/bin/minikube_

_minikube start_

_minikube status_

12. Created the Kubernetes configuration file named deploy-to-minikube.yaml. This file has Deployment and Service configuration in the single file. Took the sample configuration from the official kubernetes documentation for nginx container. Made the changes in the spec selector, template labels, container spec (changed the name, image and container port) to suit our needs.

13. Using triple hyphens splitted the deployment and service configuration. In the service configuration, mage the change in metadata, spec selector and ports

14. Using the below commands, deployed the kubernetes deployment and service

    1. _kubectl apply -f deploy-to-minikube.yaml_

15. Using the below commands, validated the deployments and service. Opened the port mentioned in the load balancer in the EC2 Security groups.

    1. _kubectl get deployments_
    2. _kubectl get svc_
    3. _kubectl get all_

16. Checked it from the browser for the main page and was able to see the json text API Documentation. Tested with Postman for the main page

Curl Command: curl --location --request GET 'http&#x3A;//54.91.77.101:4000/'

![](https://lh6.googleusercontent.com/42lq5bdCfT7ZuUpXncpgs7gXZWfKs36N8yx_uHNqDaOuG_0Z35H3vdSQHbbi4NozT7XNeIqraguAd_NpHSnNmXkP80chFeUpNtmcvz9gUFoQem6VJZGAFJSOLy64pmhN1wKbYNi-rmmQoIXB1n_dfofQ62iOs8X0Maaq0J690VklU_6XoqrYDjglHmXmlQ)

17. Tested the read ocr function from the postman.

- Made few changes in the views.py
- Added logging module to see the errors and to print other information. 

_import logging_

_logging.basicConfig(level=logging.INFO)_

- Printed the configuration like image, lang, config before the request is made to fetch the image to make sure the request is received correctly. Image is fetched and stored in the root directory, so did not join the directory named data hard coded as IMAGEPATH variable. 

_image_path __=__ os.path.__join__(image_name)_

__Below image is used for testing purposes.

![](https://lh3.googleusercontent.com/rLYhthjQhg7Ln8G_kOqqN1JU_AOrKjDZgnYmC_3DAnqLDZa74nA2vaJDC4_1T-Hs0XH1bj53TO6eVhd5k1oLAKongwZcBN5kqVGJDGGWdhfTWIxYFZcHAdRe2Q26Rg7GSq9MHVDNCrmY6JTZbx-TQ1PHNXSxOcJ9gPSVcGHEUlbIhO5uxXR6kkmluNzeiA)

  


Send the request from the postman.

Postman output

![](https://lh4.googleusercontent.com/oEA4qORU1B8yJh1gp2KsL5-WRnUeYFS9RuJxCrAjBaDv_ufIB9DSqRqOsIiykNwQRoPdGrZmvPbAcxS14Ui51GTxhlINdp35EcgsPX8XrED_U_m9PStWk2avyVKJ_--xR6B-Ur-6ROC3HUA69n7GjhhMXE81wyyvZiLZ-cGsMaz_kQVwz33BAinQ0N9uFQ)

Curl command used to send the request:

_curl --location --request POST __'http&#x3A;//54.91.77.101:4000/read_ocr'__ \\_

_--header __'Content-Type: application/json'__ \\_

_--data-raw __'{_

_    __"image"__: __"https&#x3A;//miro.medium.com/max/640/1\*t4bo8ptFFmSNbYduTCrcKg.webp"__,_

_    __"lang"__: __"eng"__,_

_    __"config"__: __""_

_}__'_


### Continuous Integration and Continuous Deployment:

CICD is achieved through Github repository and Github Actions.  

On the [Github repository](https://github.com/abdulkader4513/precily),  added two new repository secret - one named as DOCKER_HUB_USERNAME to store the username of the Docker Hub repository and second one named as DOCKER_HUB_ACCESS_TOKEN to store the password of the docker hub. 

Created a new file named main.yml in the directory .github/workflows. Basically, on every change in the main branch, github actions spin up the ubuntu container. 

Below are the steps performed in the Github Action

Step 1: Check out the repository

___        ____name: Checkout_

_        __ ____uses: actions/checkout@v3_

Step 2: Login to Docker Hub with Credentials at the Secrets which we created

_        name: Login to Docker Hub with Credentials at the Secrets_

_        uses: docker/login-action@v2_

_        with:_

_          username: ${{ secrets.DOCKER_HUB_USERNAME }}_

_          password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}_

Step 3: Instals and starts the minikube

_      __ __ name: Start minikube_

_        __ __ uses: medyagh/setup-minikube@master_

Step 4: Checking kubectl command inside the minikube

_      - name: Try the cluster !_

_        run: kubectl get pods -A _

![](https://lh3.googleusercontent.com/ZOvtl2fRPpbFFGDxhA4chT0v1bMkYNIr_VAmoZ6-YphirOZVoMBIEhehOeRXSrOWHr7qp2XLV72GlOrhyyDdz-x7_Nezi_zhHE5UtZDUZhlhuPneW1XBaQmKjI1xPrdgbpzZGvbJtxu6vjRawOQc3YKdlf8ZKoR0OfuAUKlZmXtLxdkURyqnnsyNvKxnrw)

Step 5: docker-env is used to build docker images inside the minkube. Performed docker build and tag. Listed the docker images. Pushed the image to the Docker Hub.

_        name: Build and push_

_        run: |_

_          export SHELL=/bin/bash_

_          eval $(minikube -p minikube docker-env)_

_          docker build -f ./Dockerfile -t abdulkader4513/precily ._

_          docker tag abdulkader4513/precily abdulkader4513/precily:latest_

_          docker images_

_          docker push abdulkader4513/precily:latest_

_          echo -n "verifying images:"_

![](https://lh4.googleusercontent.com/seSLpjPMdqHjEO_1CfQLIEN_lcd5oLsAZLldWtuHtjYOgnj-mw8gnmga9eIjRYiBS8amo3wVPBj_b7JQO3tFj4Ytivi0UJ9_xu3l119Gp_YLmpMFnI75puQBA_9gH444_qCeZWw33hMoC_jv_nNZVoxzVb8VKAU-yJ0gAHtEiJqr4qCWyQ5GVXsxOyV4pg)

Step 6: Deployed the Kubernetes Deployment and Service using kubectl apply on the kubernetes created configuration file deploy-to-minikube.yaml

_        name: Deploy to minikube_

_        run:_

_          kubectl apply -f deploy-to-minikube.yaml_

![](https://lh4.googleusercontent.com/rICbDmUYbVHy4CJtznlmkj4r6bEbsbSRbyhKPC0ScqaNCPhdfiXn-6pK6PWiLdS4yqPEToGtyC4DvjQpU3DEvS5aQxwlbK-grJHyO1DX_6xJ31AU3TbZvO85MVy-M-MesyufEOsSl2bvb9WR-9jtMxd4OJMKL1JX0a3vY8s-dgfAoSlO-1ENI0MKbTAncQ)

Step 7: In this stage, tested two APIs. One using a GET request and another using a POST request. In the beginning of this stage,intentionally made the container to sleep for one minute. This is because Kubernetes service takes some time to give the External IP. Then listed the service using kubectl. Got the service url of the container with the port. 

        name: Test service URLs

        run: |

          sleep 1m

          kubectl get svc

          minikube service list

          minikube service precily --url

          echo "------------------opening the service------------------"

          echo "curl $(minikube service precily --url)"

          echo "------------------TESTING ROOT FUNCTION------------------"

          curl $(minikube service precily --url)

          echo "------------------TESTING READ OCR FUNCTION------------------"

          echo "curl -X POST -H "Content-Type: application/json" -d '{"image":"https&#x3A;//miro.medium.com/max/640/1\*t4bo8ptFFmSNbYduTCrcKg.webp","lang":"eng","config":""}' $(minikube service precily --url)/read_ocr"

          curl -X POST -H "Content-Type: application/json" -d '{"image":"https&#x3A;//miro.medium.com/max/640/1\*t4bo8ptFFmSNbYduTCrcKg.webp","lang":"eng","config":""}' $(minikube service precily --url)/read_ocr

![](https://lh5.googleusercontent.com/UprrCHCuQHQkCiMy5QaFpzdU3megU9LUwRKoYrDizCEhdwK2g8dv70C-3kScsQAt3dEOSq0djkTqWV7GRAju5VKK9GANUDTxyR-tS4Di2vzVm15sVSp8RjzzG1lmSXn9EG6yFf-QCVuiFRw19WNZs-wZwohBW1EgO6iHqQ93tnnqsDhsmn16Ehl9dVhA-Q)

The above image shows the response of the root page. 

Overall, CI and CD process is completed. Step 1-5 are belongs to Continuous Integration and Step 6, Step 7 belong to Continuous deployment.


### Improvements:

1. CI and CD can be separated into two separate Github Actions. It would be great to have approval process in between them. Proposed CICD method: 

CI - Step 1 to 5  → Developer Lead/Manager → CD - Step 6 to 7 (Development Server) → Approval from Architect/Manager  → CD - Step 6 to 7 (QA Server) → QA Sign Off → Approval from Architect/Manager  → CD - Step 6 to 7 (Production Server)

2. Minikube is suitable for proof of concept and may be for development environment. It is better to go with managed Kubernetes Services like (AWS EKS, Linode LKE or something similar). 
3. Provisioning of EC2 server is performed using AWS Console. Provisioning of EC2 using Terraform is much preferred because of the state file. 
4. While performing the Flask API for read ocr, the response took almost 6 seconds average. This may make the end users to wait longer time. So it is better to go with the decoupled process meaning get the request from the end user, store the message in the queue and send the response to the user that we received your request. All the queue messages can be processed by worker servers and it can notify the end user after processing is over, deletes the message from the queue.
5. Settting minikube requires lots of installation. Ansible canhelp here to make the isntallation process easier and at scale. 

Reference:

1. Dockerfile for Python

   1. <https://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-python>

2. Kubernetes Deployment

   1. <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>

3. Kubernetes Service

   1. <https://kubernetes.io/docs/concepts/services-networking/service/>

4. Running flask application in minikube

   1. <https://thecodinginterface.com/blog/flask-rest-api-minikube/>

5. Docker and Minikube Installation on Amazon EC2

   1. <https://faun.pub/how-to-install-minikube-on-ec2-ubuntu-22-04-lts-2022-fe642d6cbc40>

6. Image used for testing read ocr API

   1. <https://miro.medium.com/max/640/1*t4bo8ptFFmSNbYduTCrcKg.webp>

7. CI/CD configuration for Python Application

   1. <https://docs.docker.com/language/python/configure-ci-cd/>

8. Minikube in Github Actions

   1. <https://minikube.sigs.k8s.io/docs/tutorials/setup_minikube_in_github_actions/>
