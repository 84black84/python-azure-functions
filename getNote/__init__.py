import logging
import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for getting only one note.')

    noteId = req.params.get('noteId')
    if not noteId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            noteId = req_body.get('noteId')

    if noteId:
        try:
            # url = "mongodb://127.0.0.1:27017"
            url = "mongodb://cma-cosmos-db-account:DTkqLNQBThSrjftegdyPbXjSG6m3yBTfRhSkPGEidExO4zTtQNJ9vqfSpz7U8W5WKadZNbrJAzKsTslAT9gDGQ==@cma-cosmos-db-account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cma-cosmos-db-account@"
            # url = os.environ['MyDbConnectionString'] -- ideally 
            client = pymongo.MongoClient(url)
            database = client["azureFunctionsTest"]
            collection = database["notes"]
            
            result = collection.find({"_id" : noteId})
            result = dumps(result)
        
            return  func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
        except ConnectionError:
            return func.HttpResponse("Unable to connect to the Mongo Db", status_code=400)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a note Id in the query string or in the request body for a personalized response.",
             status_code=200
             )