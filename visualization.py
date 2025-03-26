import matplotlib.pyplot as plt
from pymongo import MongoClient

def visualize_sentiment_distribution():
    """
    Visualize the distribution of sentiments from the MongoDB database.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sentimentDB"]
    collection = db["reviews"]

    # Fetch sentiment data
    sentiments = collection.find()
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

    for review in sentiments:
        sentiment = review["sentiment"]["label"]
        sentiment_counts[sentiment] += 1

    # Create a bar chart
    plt.bar(sentiment_counts.keys(), sentiment_counts.values())
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Analysis Distribution")
    plt.show()
