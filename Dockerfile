FROM python:3.8

# Create app directory
WORKDIR /opt/hello-app

# Install app
COPY src/* ./

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python3", "hello-world.py" ]