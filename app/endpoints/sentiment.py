from transformers import pipeline

def sentiment_analysis_score(text: str):
    sentiment_pipeline = pipeline('sentiment-analysis')
    return sentiment_pipeline(text)