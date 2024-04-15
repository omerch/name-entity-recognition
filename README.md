This repository houses a Named Entity Recognition (NER) API, leveraging
pre-trained model from spaCy to facilitate NER extraction from texts.

Prerequisite:
  -  Before running the service, ensure to create a `.env` file in the root directory. Refer to the
  `env.template` file to determine the variables that need to be set in the
  .env
  file.

### 📦 Setup

Python 3.9 is utilized for this service.

- All dependencies are listed in the` requirements.txt` file. To install them,
  execute the following command:

    ```shell
    pip install -r requirements.txt
    ```

- To launch the service and test the model via a simple REST API, execute the
  following command:
    ```shell   
    uvicorn app.main:fastapi_app --port 8000
    ```

### 📦 Build Docker Image and Running the container

 Run this command to build the image

   ```shell  
  docker build -t ner-service .
   ```

Run this command to run the docker container
   ```shell  
  docker run -d -p host_port:container_port --env-file=.env ner-service .
   ```

### 📦 Docker Compose

Deploying the application is simplified with Docker. Prior to running the
Docker image, create a `.env` file. Refer to the ` env.template` file to
identify the environment variables that need to be set in the .env file.
I
   ```

- Build & Start
   ```shell  
  docker-compose build
  docker-compose up
  ```

### Endpoints

Access all exposed endpoints via this URL: http://localhost:8000/docs/
