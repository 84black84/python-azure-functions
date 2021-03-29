import pymongo
import os

class DatabaseHelper:

    @staticmethod
    def getCollection():
        url = os.environ['MyDbConnectionString']
        client = pymongo.MongoClient(url)
        database = client["azureFunctionsTest"]
        collection = database["notes"]
        
        return collection