from pydantic import BaseModel
from typing import List

class ReviewBatch(BaseModel):
    reviews: List[str]

class SentimentResponse(BaseModel):
    overall_sentiment: str
    sentiment_score: float
    key_themes: List[str]
    actionable_feedback: str
