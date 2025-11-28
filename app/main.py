from fastapi import FastAPI
from app.schemas import ReviewBatch, SentimentResponse
from app.utils import get_sentiment, extract_themes, actionable_feedback

app = FastAPI(title="Sentiment Engine API (Free & Open Source)")

@app.post("/analyze", response_model=SentimentResponse)
def analyze_reviews(payload: ReviewBatch):
    combined_text = " ".join(payload.reviews)

    sentiment_label, sentiment_score = get_sentiment(combined_text)
    themes = extract_themes(combined_text, top_k=3)
    feedback = actionable_feedback(sentiment_label, themes)

    return {
        "overall_sentiment": sentiment_label,
        "sentiment_score": sentiment_score,
        "key_themes": themes,
        "actionable_feedback": feedback
    }
