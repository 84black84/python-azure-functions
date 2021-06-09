# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

# All the environment variables go here
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    MyDbConnectionString="mongodb://cma-cosmos-db-account:DTkqLNQBThSrjftegdyPbXjSG6m3yBTfRhSkPGEidExO4zTtQNJ9vqfSpz7U8W5WKadZNbrJAzKsTslAT9gDGQ==@cma-cosmos-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cma-cosmos-db-account@"

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot