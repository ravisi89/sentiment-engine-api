# Sentiment Engine API

A FastAPI microservice that analyzes a batch of customer reviews and returns:
- **Overall Sentiment**: `positive` / `neutral` / `negative` (with numeric score)
- **Key Themes**: top 3 keywords discussed in reviews
- **Actionable Feedback**: one-sentence deterministic recommendation

**Built with**: FastAPI, VADER (`vaderSentiment`), scikit-learn (`CountVectorizer`), and NLTK.  
Fully open-source — no paid API keys required.

---

## Repo structure
sentiment-engine-api/
├─ app/
│ ├─ init.py
│ ├─ main.py # FastAPI app (POST /analyze)
│ ├─ schemas.py # Pydantic models
│ └─ utils.py # sentiment + theme extraction + feedback
├─ requirements.txt
├─ README.md
└─ .gitignore


---

## Quick start (run locally)

1. Clone repo:
```bash
git clone https://github.com/ravisi89/sentiment-engine-api.git
cd sentiment-engine-api

2. Create & activate virtual environment (recommended):

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Start server:

uvicorn app.main:app --reload --port 8000


5. Open Swagger UI:

http://localhost:8000/docs

API (example)

POST /analyze
Request body:

{
  "reviews": [
    "I love the new feature, but the UI is too slow.",
    "Terrible support."
  ]
}


Example response:

{
  "overall_sentiment": "negative",
  "sentiment_score": -0.44,
  "key_themes": ["ui", "support", "feature"],
  "actionable_feedback": "Improve ui, support to address customer concerns."
}

Implementation notes

Sentiment: computed with VADER (compound score). Thresholds: ≥0.05 positive, ≤-0.05 negative, else neutral.

Themes: extracted using CountVectorizer with NLTK stopwords; top 3 tokens returned.

Recommendation: rule-based deterministic sentence built from sentiment + top themes. This ensures consistent JSON output — no LLM required.
