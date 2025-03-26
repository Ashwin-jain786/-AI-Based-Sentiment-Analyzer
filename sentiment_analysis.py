from transformers import pipeline

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", revision="714eb0f")


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        dict: The sentiment analysis result.
    """
    result = sentiment_analyzer(text)
    return {
        "label": result[0]["label"],
        "score": result[0]["score"]
    }
