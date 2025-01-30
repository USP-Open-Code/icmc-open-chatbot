import pytest
import pytest_asyncio
import asyncio
from src.database.mongodb.connector import MongoDB


@pytest_asyncio.fixture(scope="session")
async def mongodb() -> MongoDB:
    """Fixture for MongoDB test instance."""
    mongo = MongoDB()
    # Garantir que estamos usando o MongoDB de teste
    mongo.uri = "mongodb://localhost:27017"

    # Esperar o MongoDB inicializar
    for _ in range(5):
        try:
            await mongo.connect(db_name="test_db")
            break
        except Exception:
            await asyncio.sleep(1)
    else:
        raise Exception("Could not connect to test MongoDB")

    yield mongo

    # Cleanup
    await mongo.close()


class TestMongoDB:
    """Test suite for MongoDB connector."""
    DB_NAME = "test_db"
    COLLECTION_NAME = "test_collection"

    @pytest.mark.asyncio
    async def test_check_connection(self, mongodb):
        """Test MongoDB ping command."""
        await mongodb.check_connection()
        assert mongodb.client is not None

    @pytest.mark.asyncio
    async def test_connect(self, mongodb):
        """Test database connection."""
        await mongodb.connect(db_name=self.DB_NAME)
        assert mongodb.db is not None
        assert mongodb.client is not None

    @pytest.mark.asyncio
    async def test_connect_error(self):
        """Test connection error handling."""
        mongodb = MongoDB()
        mongodb.uri = "mongodb://invalid:27017"

        with pytest.raises(Exception) as exc_info:
            await mongodb.connect(db_name=self.DB_NAME)
        assert "Failed to connect to database" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_insert_and_find(self, mongodb):
        """Test document insertion and retrieval."""
        test_doc = {"name": "test", "value": 123}

        # Insert
        await mongodb.insert_one(self.COLLECTION_NAME, test_doc)

        # Find
        results = await mongodb.find(self.COLLECTION_NAME, {"name": "test"})
        assert len(results) > 0
        assert results[0]["name"] == "test"
        assert results[0]["value"] == 123

    @pytest.mark.asyncio
    async def test_update_one(self, mongodb):
        """Test document update."""
        # Insert test document
        test_doc = {"name": "update_test", "value": 456}
        await mongodb.insert_one(self.COLLECTION_NAME, test_doc)

        # Update
        update = {"$set": {"value": 789}}
        await mongodb.update_one(
            self.COLLECTION_NAME,
            {"name": "update_test"},
            update
        )

        # Verify
        results = await mongodb.find(
            self.COLLECTION_NAME,
            {"name": "update_test"}
        )
        assert len(results) > 0
        assert results[0]["value"] == 789

    @pytest.mark.asyncio
    async def test_delete_one(self, mongodb):
        """Test document deletion."""
        # Insert test document
        test_doc = {"name": "delete_test"}
        await mongodb.insert_one(self.COLLECTION_NAME, test_doc)

        # Delete
        await mongodb.delete_one(self.COLLECTION_NAME, {"name": "delete_test"})

        # Verify
        results = await mongodb.find(
            self.COLLECTION_NAME,
            {"name": "delete_test"}
        )
        assert len(results) == 0
