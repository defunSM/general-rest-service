import re

from typing import List
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def strip_punctuation(text: str) -> str:
    """ Removes any punctuations from text and returns the punctuation free text.

    Args:
        text (str): text that needs to be stripped of punctuation.

    Returns:
        str: text that does not have any punctuation.
    """
    
    stripped_text = re.sub(pattern = "[^\w\s]",
                           repl = "",
                           string = text)
    
    return stripped_text
    
def strip_gaps(text: str) -> str:
    """ Replaces all tabs and newlines (gaps) in text to a single space. """
    
    new_text = re.sub(pattern = '[\t\n]', 
                      repl = '',
                      string = text)
    
    return new_text

def strip_articles(tokenized_words: List[str]) -> str:
    """ Use nltk's stopwords corpus to filter out articles from text."""
    
    text_without_articles = [word for word in tokenized_words if not word in stopwords.words()]
    
    return text_without_articles