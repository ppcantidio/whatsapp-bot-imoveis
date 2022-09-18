import os
import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ.get("LOCAL_CONNECTION"))
        self.db = self.client.get_database(os.environ.get("DB_NAME"))

    def insert_object(self, object_dictionary, collection):
        collection = self.db.get_collection(collection)
        collection.insert_one(object_dictionary)

    def select_object(self, collection, where):
        collection = self.db.get_collection(collection)
        results = list(collection.find(where))
        return results
