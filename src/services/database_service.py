import os
import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ.get("LOCAL_CONNECTION"))
        self.db = self.client.get_database(os.environ.get("DB_NAME"))

    def insert_object(self, object_dictionary, collection):
        collection = self.db.get_collection(collection)
        collection.insert_one(object_dictionary)

    def select_one_object(self, collection, where):
        collection = self.db.get_collection(collection)
        results = collection.find_one(where)
        return results

    def select_one_object_sort(self, collection, where):
        collection = self.db.get_collection(collection)
        results = collection.find_one(where)
        return results

    def select_col(self, collection, where={}):
        coll = self.db.get_collection(collection)

        return coll.find(where)
