
# backend/app/sentiment_model.py
from textblob import TextBlob

def analyze_sentiment(text: str):
    """
    Analyzes the sentiment of the given text using TextBlob.
    Returns 'positive', 'negative', or 'neutral' along with a polarity score.
    """
    analysis = TextBlob(text)
    
    # Define thresholds for classification
    if analysis.sentiment.polarity > 0:
        sentiment = "positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
        
    return {
        "text": text,
        "sentiment": sentiment,
        "polarity": analysis.sentiment.polarity,
        "subjectivity": analysis.sentiment.subjectivity
    }

# if __name__ == "__main__":
#     # Example usage for testing
#     print(analyze_sentiment("This is a fantastic product!"))
#     print(analyze_sentiment("I hate this terrible movie."))
#     print(analyze_sentiment("The weather is okay today."))
    
