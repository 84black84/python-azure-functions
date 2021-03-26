import logging
import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for getting all notes!')
    try:
        url = os.environ['MyDbConnectionString']
        client = pymongo.MongoClient(url)
        database = client["azureFunctionsTest"]
        collection = database["notes"]
        
        result = collection.find({})
        result = dumps(result)
        
        return  func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except ConnectionError:
        return func.HttpResponse("Unable to connect to the Mongo Db", status_code=400)
