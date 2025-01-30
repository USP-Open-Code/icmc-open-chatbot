import pytest
import pytest_asyncio
from unittest.mock import MagicMock, patch
from src.database.mongodb.connector import MongoDB


@pytest_asyncio.fixture
async def mongodb():
    """Fixture for MongoDB instance with mocked client."""
    mongo = MongoDB()
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_admin = MagicMock()

    # Setup mock hierarchy
    mock_client.admin = mock_admin
    mock_client.__getitem__.return_value = mock_db
    mock_admin.command = MagicMock()

    # Setup MongoDB instance
    mongo.client = mock_client
    mongo.db = mock_db

    return mongo


class TestMongoDB:
    """Test suite for MongoDB connector."""
    DB_NAME = "test_db"
    COLLECTION_NAME = "test_collection"

    @pytest.mark.asyncio
    async def test_check_connection(self):
        """Test MongoDB ping command."""
        mongodb = MongoDB()

        with patch('src.database.mongodb.connector.MongoClient') as mock_client_class:
            mock_client = MagicMock()
            mock_admin = MagicMock()
            mock_command = MagicMock()

            mock_client.admin = mock_admin
            mock_admin.command = mock_command
            mock_client_class.return_value = mock_client

            await mongodb.check_connection()

            mock_client_class.assert_called_once_with(mongodb.uri)
            mock_command.assert_called_once_with('ping')

    @pytest.mark.asyncio
    async def test_connect(self):
        """Test database connection."""
        mongodb = MongoDB()

        with patch('src.database.mongodb.connector.MongoClient') as mock_client_class:
            mock_client = MagicMock()
            mock_db = MagicMock()
            mock_client.__getitem__.return_value = mock_db
            mock_client_class.return_value = mock_client

            await mongodb.connect(db_name=self.DB_NAME)

            mock_client_class.assert_called_once_with(mongodb.uri)
            mock_client.__getitem__.assert_called_once_with(self.DB_NAME)
            assert mongodb.db == mock_db

    @pytest.mark.asyncio
    async def test_connect_error(self):
        """Test connection error handling."""
        mongodb = MongoDB()
        error_msg = "Connection failed"

        with patch('src.database.mongodb.connector.MongoClient',
                  side_effect=Exception(error_msg)):
            with pytest.raises(Exception) as exc_info:
                await mongodb.connect(db_name=self.DB_NAME)
            assert "Failed to connect to database" in str(exc_info.value)
            assert mongodb.client is None
            assert mongodb.db is None

    @pytest.mark.asyncio
    async def test_close(self):
        """Test connection closure."""
        mongodb = MongoDB()
        mock_client = MagicMock()
        mongodb.client = mock_client

        await mongodb.close()

        mock_client.close.assert_called_once()
        assert mongodb.client is None
        assert mongodb.db is None

    @pytest.mark.asyncio
    async def test_get_collection(self):
        """Test collection retrieval."""
        mongodb = MongoDB()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mongodb.db = mock_db
        mock_db.__getitem__.return_value = mock_collection

        collection = mongodb.get_collection(self.COLLECTION_NAME)
        assert collection is not None
        mock_db.__getitem__.assert_called_once_with(self.COLLECTION_NAME)

    @pytest.mark.asyncio
    async def test_get_collection_no_connection(self):
        """Test collection retrieval without connection."""
        mongodb = MongoDB()
        with pytest.raises(Exception) as exc_info:
            mongodb.get_collection(self.COLLECTION_NAME)
        assert "Database connection not established" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_insert_one(self):
        """Test document insertion."""
        mongodb = MongoDB()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mongodb.db = mock_db
        mock_db.__getitem__.return_value = mock_collection

        test_doc = {"name": "test"}
        await mongodb.insert_one(self.COLLECTION_NAME, test_doc)
        mock_collection.insert_one.assert_called_once_with(test_doc)

    @pytest.mark.asyncio
    async def test_find(self):
        """Test document query."""
        mongodb = MongoDB()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mongodb.db = mock_db
        mock_db.__getitem__.return_value = mock_collection

        test_filter = {"name": "test"}
        expected_docs = [{"name": "test", "_id": 1}]
        mock_collection.find.return_value = expected_docs

        result = await mongodb.find(self.COLLECTION_NAME, test_filter)
        assert result == expected_docs
        mock_collection.find.assert_called_once_with(test_filter)

    @pytest.mark.asyncio
    async def test_update_one(self):
        """Test document update."""
        mongodb = MongoDB()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mongodb.db = mock_db
        mock_db.__getitem__.return_value = mock_collection

        test_filter = {"name": "test"}
        test_update = {"$set": {"name": "updated"}}

        await mongodb.update_one(self.COLLECTION_NAME, test_filter, test_update)
        mock_collection.update_one.assert_called_once_with(test_filter,
                                                         test_update)

    @pytest.mark.asyncio
    async def test_delete_one(self):
        """Test document deletion."""
        mongodb = MongoDB()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mongodb.db = mock_db
        mock_db.__getitem__.return_value = mock_collection

        test_filter = {"name": "test"}

        await mongodb.delete_one(self.COLLECTION_NAME, test_filter)
        mock_collection.delete_one.assert_called_once_with(test_filter)
