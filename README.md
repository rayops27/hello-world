# Hello World

Using your favorite language Go, Python, Java, Scala, Bash, etc., create a hello world application
that greets a user with `Hello!` and exposes a health status endpoint.

1. Application url should return a greeting such as `hello` 
2. Application should provide a health endpoint that returns HTTP status which indicates health of the app
and return a valid json with the following information:
   - `status`: status of the app: online, success, OK, error, etc.  
   - `version`: running application version (ex: 0.0.1)  
   - `uptime`: time duration or time stamp since the app is running (ex: running since YYYY-MM-DD hh:mm:ss)  
3. What other information would you add to health endpoint json object in step 2 and explain what would be the use case 
for that extra information?
4. How would you test this application? (think about automating tests)  
5. Create a docker file to build, package, deploy, and run this application locally with Docker.  
6. Setup a local (or on your favorite cloud provider) CICD pipeline with Jenkins or other CI tools to build and deploy this application 
to a local or remote docker or k8s platform.
7. What other stages would you add to the CICD pipeline if you are deploying this application to a production environment?  

Your solution should include a README explaining how to set up and run the application.

