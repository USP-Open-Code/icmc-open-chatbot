from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import os


class MongoDB:
    def __init__(self):
        self.client: MongoClient = None
        self.db: Database = None
        self.uri: str = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')

    async def check_connection(self) -> None:
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command('ping')
        except Exception as error:
            raise Exception("Error connecting to MongoDB") from error

    async def connect(self, db_name: str) -> None:
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[db_name]
        except Exception as error:
            raise error

    async def close(self) -> None:
        try:
            if self.client:
                self.client.close()
        except Exception as error:
            raise error

    def get_collection(self, collection_name: str) -> Collection:
        if not self.db:
            msg = 'Database connection not established. Call connect() first.'
            raise Exception(msg)
        return self.db[collection_name]

    async def insert_one(self, collection_name: str, document: dict) -> None:
        try:
            collection = self.get_collection(collection_name)
            collection.insert_one(document)
        except Exception as error:
            raise error

    async def find(
        self,
        collection_name: str,
        filter_query: dict
    ) -> List[dict]:
        try:
            collection = self.get_collection(collection_name)
            return list(collection.find(filter_query))
        except Exception as error:
            raise error

    async def update_one(
        self,
        collection_name: str,
        filter_query: dict,
        update: dict
    ) -> None:
        try:
            collection = self.get_collection(collection_name)
            collection.update_one(filter_query, update)
        except Exception as error:
            raise error

    async def delete_one(self, collection_name: str, filter_query: dict):
        try:
            collection = self.get_collection(collection_name)
            collection.delete_one(filter_query)
        except Exception as error:
            raise error
