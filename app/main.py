from typing import Union

from fastapi import FastAPI

from app.countleaf import main

app = FastAPI(title="General Rest API")

#TODO: Fix strip_articles from text_summary

@app.get("/")
def read_root():
    string = """
    Physics is the natural science that studies matter,[a] its fundamental the constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, with its main goal being to understand how the universe behaves. A scientist who specializes in the field of physics is called a physicist.
    """
    return main.text_summary(string)

@app.get("/countleaf/summary/")
def read_text(text: str, articles: int = 0):
    """ Returns a summary of the string including how many words, letters, sentences, letters / word, words / sentence, most frequent word within the block of text including compute time.

    Args:
        text (str): The block of text that is being computed.
        articles (bool): Determines whether to count articles or remove them (0 by default is to include them)
        
    Returns:
        dict: A summary of the text.
    """
    return main.text_summary(text, articles)