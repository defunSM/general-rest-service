from typing import Union

from fastapi import FastAPI

from countleaf import main


app = FastAPI(title="Countleaf API",
              description="Countleaf API provides an online web service for natural language processing and text analysis. Including evaluating text similarity, sentiment analysis and general text analytics.",
              version="1.0.0",
              contact={"name": "Salman Hossain", 
                       "url": "https://defunsm.com/countleaf",
                       "email": "salmanhossain500@gmail.com",})

#TODO: Fix strip_articles from text_summary

@app.get("/")
def read_root():
    string = """
    Physics is the natural science that studies matter,[a] its fundamental the constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, with its main goal being to understand how the universe behaves. A scientist who specializes in the field of physics is called a physicist.
    """
    
    return main.text_summary(string)

@app.get("/countleaf/v1/summary/")
def read_text_summary(text: str, articles: bool = False, url: bool = False):
    """ Returns a summary of the text including:
    
    ✅ Words 
    
    ✅ Letters
    
    ✅ Sentences
    
    ✅ Letters per Word
    
    ✅ Words per Sentence
    
    ✅ Most Frequent Word
    
    ✅ Compute Time

    Args:
        text (str): The block of text that is being computed.
        articles (bool): Determines whether to count articles or remove them (0 by default is to include them)
        
    Returns:
        dict: A summary of the text.
    """
    
    return main.text_summary(text, articles, url)

@app.get("/countleaf/v1/similarity")
def text_similarity(text1: str, text2: str):
    """ Returns the similarity between text1 and text2 using Levenshtein distance.

    **Args:**
        
        text1 (str): The first section of text
        
        text2 (str): The second section of text

    **Returns:**
    
        similarity_score (int): An integer representing the similarity between 0 - 100
    """
    return main.text_similarity(text1, text2)

@app.get("/countleaf/v1/sentiment")
def sentiment_analysis(text: str):
    """ Uses the **distilbert-base-uncased-finetuned-sst-2-english** model to classify the sentiment of a piece of text.

    **Args:**
        
        text (str): A section of text.

    **Returns:**
    
        sentiment_score (JSON): Contains the label (positive or negative) and the score (between 0 and 1) 
    """
    return main.sentiment_analysis(text)
    