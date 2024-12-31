from pymongo import MongoClient,errors
from app.config import MONGO_URI, DATABASE_NAME
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    print(f"Connected to database: {DATABASE_NAME}")
except errors.ConnectionFailure as e:
    print(f"Error connecting to database: {e}")


def get_collection(name: str):
    """
    Returns a collection from the MongoDB database.
    """
    return db[name]

def is_db_connected():
    """Check if the database connection is active."""
    try:
        # The `ping` command is used to check the connection
        client.admin.command("ping")
        return True
    except ConnectionFailure:
        return False
