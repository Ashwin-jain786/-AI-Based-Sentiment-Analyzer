from pymongo import MongoClient, errors

class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="sentimentDB"):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            print("MongoDB connected successfully!")
        except errors.ConnectionFailure as e:
            print(f"Error: {e}")

    def insert_review(self, review_text, sentiment):
        """
        Insert a review and its sentiment into the database.
        
        Args:
            review_text (str): The text of the review.
            sentiment (dict): The sentiment analysis result.
        """
        collection = self.db["reviews"]
        collection.insert_one({"text": review_text, "sentiment": sentiment})
