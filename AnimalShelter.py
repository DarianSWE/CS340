from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        USER = 'aacuser'
        PASS = 'password_1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32296
        DB = 'AAC'
        COL = 'animals'

        # MongoDB Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """
        Inserts a document into the collection.
        Returns True if successful, else False.
        """
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"Insert failed: {e}")
                return False
        else:
            raise ValueError("No data provided to insert.")

    def read(self, query):
        """
        Queries documents from the collection.
        Returns a list of results or an empty list.
        """
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Read failed: {e}")
            return []

    def update(self, query, update_values):
        """
        Updates one or more documents that match the query.
        Returns the number of documents modified.
        """
        if not query or not update_values:
            raise ValueError("Both query and update_values must be provided.")

        try:
            result = self.collection.update_many(query, {"$set": update_values})
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0

    def delete(self, query):
        """
        Deletes one or more documents that match the query.
        Returns the number of documents deleted.
        """
        if not query:
            raise ValueError("Query must be provided for delete operation.")

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0
