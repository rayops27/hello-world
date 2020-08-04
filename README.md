# Hello World

Using your favorite language (Go, Python, Java, Scala, Bash, etc.), create a hello world web application API
that listens on port 8080 and greets a user with `Hello!` and exposes a health status endpoint.

1. Application url should return a greeting such as `Hello!` as json or plain text (ex: when you open a browser and navigate to http://localhost:8080 it should `Hello!` plain text.)
2. Application should provide a health endpoint (http://localhost:8080/healthz) that returns HTTP status (200 OK)
which indicates health of the application and return a valid json with the following information:
   - `status`: status of the app: online, success, OK, error, etc.  
   - `version`: running application version (ex: 0.0.1)  
   - `uptime`: time duration or time stamp since the app is running (ex: running since YYYY-MM-DD hh:mm:ss)
  Example: When you open a browser and navigate to http://localhost:8080/healthz it should return:
  ```
  {
    "status": "OK",
    "version": "0.0.1",
    "uptime": "up since 2020-08-04 08:00:05"
  }
  ```
3. What other information would you add to health endpoint json object in step 2 and explain what would be the use case
for that extra information?
4. Create a docker file to build, package, deploy, and run this application locally with Docker.    
5. Setup a local (or on your favorite cloud provider) CICD pipeline with Jenkins or other CI tools to build and deploy this application
to a local or remote docker or k8s platform. If you choose to set Jenkins pipeline in your local laptop,
 docker compose can be used to start all components and test.
6. What other stages would you add to the CICD pipeline if you are deploying this application to a production environment?  


Your solution should include a README explaining how to set up and run the application.
