import logging
import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps
from databaseHelper import DatabaseHelper

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
            collection = DatabaseHelper.getCollection()
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