from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status

from countleaf import main
from countleaf import security

app = FastAPI(title="Countleaf API",
              description="Countleaf API 🍁 provides an online web service for natural language processing and text analysis. Including evaluating text similarity, sentiment analysis and general text analytics.",
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

@app.get("/countleaf/v1/summary", tags=["countleaf v1"])
def read_text_summary(text: str, articles: bool = False, url: bool = False):
    """ Returns a summary of the text including:
    
    ✅ Words 
    
    ✅ Letters
    
    ✅ Sentences
    
    ✅ Letters per Word
    
    ✅ Words per Sentence
    
    ✅ Most Frequent Word
    
    ❌ Compute Time
    
    ❌ Cached

    **Args:**
    
        text (str): The block of text that is being computed.
        articles (bool): Determines whether to count articles or remove them (0 by default is to include them)
        
    **Returns:**
    
        dict: A summary of the text.
    """
    
    return main.text_summary(text, articles, url)

@app.get("/countleaf/v1/similarity", tags=["countleaf v1"])
def text_similarity(text1: str, text2: str):
    """ Returns the similarity between text1 and text2 using Levenshtein distance.

    **Args:**
        
        text1 (str): The first section of text
        
        text2 (str): The second section of text

    **Returns:**
    
        similarity_score (int): An integer representing the similarity between 0 - 100
    """
    return main.text_similarity(text1, text2)

@app.get("/countleaf/v1/sentiment", tags=["countleaf v1"])
def sentiment_analysis(text: str, token: str = Depends(security.oauth2_scheme)):
    """ Uses the **distilbert-base-uncased-finetuned-sst-2-english** model to classify the sentiment of a piece of text.

    **Args:**
        
        text (str): A section of text.

    **Returns:**
    
        sentiment_score (JSON): Contains the label (positive or negative) and the score (between 0 and 1) 
    """
    return main.sentiment_analysis(text)

@app.get("/countleaf/v1/testauth", tags=["test"])
def test_autherization(token: str = Depends(security.oauth2_scheme)):
    return {"Test: Works"}

@app.post("/token", response_model=security.Token)
async def login_for_access_token(form_data: security.OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(security.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = security.timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=security.User)
async def read_users_me(current_user: security.User = Depends(security.get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: security.User = Depends(security.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]