
import re

from typing import List
from nltk.tokenize import word_tokenize

from helpers import strip_articles, strip_gaps, strip_punctuation

# TODO: Stripping punctuation twice in count_words and count_letters try to apply dry principle

def count_frequent_word(text: str) -> str:
    pass

def count_sentences(text: str) -> int:
    """ Counts the sentences based on how many periods there are after a alpha
    """

def count_letters(text: str) -> int:
    
    text = strip_punctuation(text)
    
    # Removes spaces from the text so only characters are left
    text = text.replace(" ", "")
    
    return len(text.split())

def count_words(text):
    """Counts the number of words in each string. Will ignore punctuation"""
    
    # Remove away the punctuations in the text
    text = strip_punctuation(text)
    
    # Create an array of words
    text = word_tokenize(text)
    
    return len(text)
    

def text_summary(text: str, articles: bool = 0) -> dict:
    """ Returns a summary of the string including how many words, letters, sentences, letters / word, words / sentence, most frequent word within the block of text including compute time.

    Args:
        text (str): The block of text that is being computed.
        articles (bool): Determines whether to count articles or remove them (0 by default is to include them)
        
    Returns:
        dict: _description_
    """
    if articles:
        text = "".join(strip_articles(text))
    
    words = count_words(text)
    letters = count_letters(text)
    sentences = count_sentences(text)
    letters_per_word = letters / words
    words_per_sentence = words / sentences 
    most_frequent_word = count_frequent_word(text)
    
    pass

if __name__ == '__main__':
    test = """
    sadfas sadas i they myself ....
    asdas
    man out here 
    """
    print(strip_articles(test))