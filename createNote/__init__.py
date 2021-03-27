import logging
import azure.functions as func
import pymongo
import json
import os

def main(request: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    requestObject = request.get_json()

    if requestObject:
        try:
            # add your connection string here
            url = os.environ['MyDbConnectionString']
            client = pymongo.MongoClient(url)

            # you will need this fill in
            database = client["azureFunctionsTest"]
            collection = database["notes"]

            # replace the insert_one variable with what you think should be in the bracket
            # newNote = json.load(requestObject)

            title = requestObject.get('title')
            description = requestObject.get('desc')
            collection.insert_one({"title" : title, "desc": description})

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(request.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object", status_code=400)