
import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, '..', 'app')
sys.path.insert(0, app_dir)

from model import analyze_sentiment

def test_positive_sentiment():
    """
    Test case for positive sentiment text.
    """
    text = "This product is absolutely amazing! I love it."
    result = analyze_sentiment(text)
    assert result["sentiment"] == "positive"
    assert result["polarity"] > 0

def test_negative_sentiment():
    """
    Test case for negative sentiment text.
    """
    text = "This is a terrible experience, very disappointing."
    result = analyze_sentiment(text)
    assert result["sentiment"] == "negative"
    assert result["polarity"] < 0

def test_neutral_sentiment():
    """
    Test case for neutral sentiment text.
    """
    text = "The sky is blue today."
    result = analyze_sentiment(text)
    assert result["sentiment"] == "neutral"
    assert result["polarity"] == 0

def test_mixed_sentiment():
    """
    Test case for text with mixed sentiment (should lean towards overall dominant).
    """
    text = "It started badly, but then it got much better and I enjoyed it."
    result = analyze_sentiment(text)
    # TextBlob might lean positive here due to "much better" and "enjoyed"
    assert result["sentiment"] == "positive"
    assert result["polarity"] > 0

def test_empty_string():
    """
    Test case for an empty string input.
    TextBlob handles empty strings by returning 0 polarity and 0 subjectivity.
    Our function should classify this as neutral.
    """
    text = ""
    result = analyze_sentiment(text)
    assert result["sentiment"] == "neutral"
    assert result["polarity"] == 0
    assert result["subjectivity"] == 0

def test_punctuation_and_casing():
    """
    Test case for text with varying punctuation and casing.
    """
    text = "i love this! it's SO good!!!"
    result = analyze_sentiment(text)
    assert result["sentiment"] == "positive"
    assert result["polarity"] > 0

def test_numeric_input():
    """
    Test case for numeric input (should be treated as neutral text).
    """
    text = "12345"
    result = analyze_sentiment(text)
    assert result["sentiment"] == "neutral"
    assert result["polarity"] == 0
    
