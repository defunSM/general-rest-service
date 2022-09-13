
import re
from typing import List

from helpers import strip_articles, strip_gaps, strip_punctuation

def count_sentences(text: str) -> str:
    """ Counts the sentences based on how many periods there are after a alpha
    """

def count_words(text):
    """Counts the number of words in each string. Will ignore punctuation"""

def text_summary(text: str) -> dict:
    """ Returns a summary of the string including how many words, letters, sentences, letters / word, words / sentence, most frequent word within the block of text including compute time.

    Args:
        string (str): The block of text that is being computed.

    Returns:
        dict: _description_
    """
    pass

if __name__ == '__main__':
    test = """
    sadfas sadas
    asdas
    man out here 
    """
    print(strip_gaps(test))