# Hello World
**prerequisite**

Install docker <br />
git


 1. Clone repo and run command to run hello-world api  
 Build docker image <br />
    **docker build -t my-hello-world .** <br /> <br />
 Run docker container <br />
     **docker run -d my-hello-world -p 8080:8080**
 
Open http://localhost:8080 in browser to say hello!! <br /> <br />
 
 
 2. Application will print HTTPS status (http://localhost:8080/healthz) <br />
 
 3. we can get extra information like CPU, Memory, Disk usage of system 
 4. Docker file created which build images and deploy api app
 5. We can automate build/test/deploy api app using Version control, Jenkins, Artifactoyr/Registry to store app versions
   We need to can write jenkins declarative pipeline with build stages build, test, deploy as example in Jenkins file
   a. We can use branch model Master, develop, release-2020-08-24, bug-fix, 
     Where individual contributors submit pull request to develop branch and runs builds and unit level testing and deployment to testing env once build success deploy promote build to higher environments as upstream jenkins jobs
     and we can cut release branch once changes freeze for production deployment  with release cadence.
     develop<===Pull Request (success on merge), cut release branches from develop.
    b. I used VCS-GIT(Gitlab, Github), Jenkins, Artifactory, Ansible
    c. We would have Build,Test-integration and quality,deployment, sanity checks <br />
    d. Purpose of each stage of build to compile, package and deploy app which refines quality of app/service
    
 6.  Build docker image <br />
        **docker build -t my-hello-world .** <br /> <br />
     Run docker container <br />
         **docker run -d my-hello-world -p 8080:8080**
     
    Open http://localhost:8080 in browser to say hello!!
     
     