from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
import os

from src.infrastructure.config import settings


class MongoDB:
    def __init__(self, db_name: str = None):
        """Initialize MongoDB connector with default configuration.

        Attributes:
            client (MongoClient): MongoDB client instance
            db (Database): Selected database instance
            uri (str): MongoDB connection URI, defaults to localhost if MONGODB_URI env var not set
        """
        self.client: MongoClient = None
        self.db: Database = None
        self.uri: str = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')

        if self.check_connection():
            self.connect(db_name or settings.MONGO_DB)

    async def check_connection(self) -> None:
        """Check MongoDB connection by sending a ping command.

        Raises:
            Exception: If connection fails or ping command fails
        """
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command('ping')
        except Exception as error:
            self.client = None
            raise Exception("Error connecting to MongoDB") from error

    async def connect(self, db_name: str) -> None:
        """Connect to MongoDB and select database.

        Args:
            db_name (str): Name of the database to connect to

        Raises:
            Exception: If connection fails or database selection fails
        """
        try:
            self.client = MongoClient(self.uri)
            if db_name not in self.client.list_database_names():
                raise ValueError(f"The database '{db_name}' does not exist!")
            self.db = self.client[db_name]

        except Exception as error:
            raise ConnectionError(f"Failed to connect to database: {error}")

    async def close(self) -> None:
        """Close MongoDB connection and reset client/db attributes.

        Raises:
            Exception: If closing the connection fails
        """
        try:
            if self.client:
                self.client.close()
                self.client = None
                self.db = None
        except Exception as error:
            raise Exception("Error closing connection") from error

    def get_collection(self, collection_name: str) -> Collection:
        """Get a MongoDB collection by name.

        Args:
            collection_name (str): Name of the collection to retrieve

        Returns:
            Collection: MongoDB collection object

        Raises:
            Exception: If database connection is not established
        """
        if not self.db:
            msg = 'Database connection not established. Call connect() first.'
            raise Exception(msg)
        return self.db[collection_name]

    async def insert_one(self, collection_name: str, document: dict) -> None:
        """Insert a single document into a collection.

        Args:
            collection_name (str): Name of the collection to insert into
            document (dict): Document to insert

        Raises:
            Exception: If insertion fails or collection does not exist
        """
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
        """Find documents in a collection matching a filter query.

        Args:
            collection_name (str): Name of the collection to search
            filter_query (dict): Query filter to apply

        Returns:
            List[dict]: List of matching documents

        Raises:
            Exception: If query fails or collection does not exist
        """
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
        """Update a single document in a collection.

        Args:
            collection_name (str): Name of the collection containing the document
            filter_query (dict): Query to find document to update
            update (dict): Update operations to apply

        Raises:
            Exception: If update fails or collection does not exist
        """
        try:
            collection = self.get_collection(collection_name)
            collection.update_one(filter_query, update)
        except Exception as error:
            raise error

    async def delete_one(self, collection_name: str, filter_query: dict):
        """Delete a single document from a collection.

        Args:
            collection_name (str): Name of the collection containing the document
            filter_query (dict): Query to find document to delete

        Raises:
            Exception: If deletion fails or collection does not exist
        """
        try:
            collection = self.get_collection(collection_name)
            collection.delete_one(filter_query)
        except Exception as error:
            raise error
