"""
This contains all the endpoints of the countleaf API.
"""

# pylint: disable=[line-too-long]

from typing import Union

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse

from endpoints import security
from endpoints.sentiment import sentiment_analysis_score
from endpoints.similarity import text_similarity_score
from endpoints.textsummary import text_summary

app = FastAPI(
    title="Countleaf API",
    description="Countleaf API 🍁 provides an online web service for natural language processing and text analysis. Including evaluating text similarity, sentiment analysis and general text analytics.",
    version="1.0.0",
    contact={
        "name": "Salman Hossain",
        "url": "https://defunsm.com/countleaf",
        "email": "salmanhossain500@gmail.com",
    }
)


@app.get("/", tags=["auth"], summary="Redirects to documentation")
def read_root():
    """ Redirects the root to the documentation."""
    return RedirectResponse("/docs")


@app.get("/countleaf/v1/summary", tags=["countleaf v1"])
def read_text_summary(text: str, articles: bool = False, url: bool = False):
    """Returns a summary of the text including:

    ✅ Words \n
    ✅ Letters \n
    ✅ Sentences \n
    ✅ Letters per Word \n
    ✅ Words per Sentence \n
    ✅ Most Frequent Word \n
    ❌ Compute Time \n
    ❌ Cached \n

    **Args:**

        text (str): The block of text that is being computed.
        articles (bool): Count articles or remove them (default: 0 is include)

    **Returns:**

        dict: A summary of the text.
    """

    return text_summary(text, articles, url)


@app.get("/countleaf/v1/similarity", tags=["countleaf v1"])
def text_similarity(text1: str, text2: str):
    """Returns the similarity between text1 and text2 using Levenshtein distance.

    **Args:**

        text1 (str): The first section of text

        text2 (str): The second section of text

    **Returns:**

        similarity_score (int): An integer representing the similarity between 0 - 100
    """
    return text_similarity_score(text1, text2)


@app.get("/countleaf/v1/sentiment", tags=["countleaf v1"])
def sentiment_analysis(text: str, _token: str = Depends(security.oauth2_scheme)):
    """**distilbert-base-uncased-finetuned-sst-2-english** model to get the sentiment of the text.

    **Args:**

        text (str): A section of text.

    **Returns:**

        sentiment_score (JSON): A label (positive or negative) and the score (between 0 and 1)
    """
    return sentiment_analysis_score(text)


@app.get("/countleaf/v1/testauth", tags=["test"])
def test_authorization(_token: str = Depends(security.oauth2_scheme)):
    """ Endpoint to test that authorization works."""
    return {"Test: Works"}


@app.post("/token", response_model=security.Token, tags=["auth"])
async def login_for_access_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
):
    """ Endpoint for dealing with login to get access token."""
    user = security.authenticate_user(
        security.fake_users_db, form_data.username, form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = security.timedelta(
        minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = security.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=security.User, tags=["test"])
async def read_users_me(
    current_user: security.User = Depends(security.get_current_active_user),
):
    """Get user settings from database."""
    return current_user


@app.get("/users/me/items/", tags=["test"])
async def read_own_items(
    current_user: security.User = Depends(security.get_current_active_user),
):
    """ Read user items from database. """
    return [{"item_id": "Foo", "owner": current_user.username}]


@app.post(
    "/signup", summary="Create new user", response_model=security.User, tags=["auth"]
)
async def sign_up(data: security.User):
    """ Endpoint that handles sign up for new users."""
    user = security.get_user(security.fake_users_db, data.username)

    user: Union[security.User, None]

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
        )

    new_user = {
        "username": data.username,
        "email": data.email,
        "full_name": data.full_name,
        "password": security.get_password_hash(data.password),
        "disabled": data.disabled,
    }

    security.fake_users_db[data.username] = new_user

    return new_user

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
