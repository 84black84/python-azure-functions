import logging
import azure.functions as func
import pymongo
import json
import os
from databaseHelper import DatabaseHelper
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for getting all notes!')
    try:
        collection = DatabaseHelper.getCollection()
        notes = collection.find({})
        notesList = list(notes)
        i = 1
        for note in notesList:
            note['title'] += '_test'+'_' + str(i)
            i+=1
        notes = dumps(notesList)      
        return  func.HttpResponse(notes, mimetype="application/json", charset='utf-8', status_code=200)
    except ConnectionError:
        return func.HttpResponse("Unable to connect to the Mongo Db", status_code=400)
