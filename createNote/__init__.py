import logging
import azure.functions as func
import pymongo
import json
import os
from databaseHelper import DatabaseHelper

def main(request: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    requestObject = request.get_json()

    if requestObject:
        try:
            title = requestObject.get('title')
            description = requestObject.get('desc')
            
            collection = DatabaseHelper.getCollection()
            collection.insert_one({"title" : title, "desc": description})

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(request.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object", status_code=400)