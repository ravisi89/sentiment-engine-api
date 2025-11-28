import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

# Ensure NLTK stopwords exist
try:
    stopwords.words("english")
except:
    nltk.download("stopwords")

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text: str):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        label = "positive"
    elif score <= -0.05:
        label = "negative"
    else:
        label = "neutral"
    return label, round(score, 3)


def extract_themes(text: str, top_k=3):
    text = text.lower()
    vectorizer = CountVectorizer(
        stop_words=stopwords.words("english"),
        max_features=30
    )
    X = vectorizer.fit_transform([text])
    vocab = vectorizer.get_feature_names_out()
    freqs = X.toarray().flatten()

    sorted_tokens = [x for _, x in sorted(zip(freqs, vocab), reverse=True)]
    return sorted_tokens[:top_k]


def actionable_feedback(sentiment: str, themes: list):
    if not themes:
        themes = ["product", "service"]

    if sentiment == "negative":
        return f"Improve {', '.join(themes[:2])} to address customer concerns."
    elif sentiment == "positive":
        return f"Customers appreciate {', '.join(themes[:2])}; highlight these strengths."
    else:
        return f"Explore enhancements in {', '.join(themes[:2])} to improve user experience."
