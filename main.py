from typing import Union

from fastapi import FastAPI

from countleaf import main

app = FastAPI(title="Hygieia App")

#TODO: Fix strip_articles from text_summary

@app.get("/")
def read_root():
    string = """
    Physics is the natural science that studies matter,[a] its fundamental the constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, with its main goal being to understand how the universe behaves. A scientist who specializes in the field of physics is called a physicist.
    """
    return main.text_summary(string)

@app.get("/countleaf/summary/")
def read_item(text: str, articles: int = 0):
    return main.text_summary(text, articles)