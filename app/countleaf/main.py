import re
import urllib.request

from nltk.tokenize import word_tokenize
from collections import Counter
from thefuzz import fuzz

from transformers import pipeline

from bs4 import BeautifulSoup

from .helpers import strip_articles, strip_gaps, strip_punctuation

# TODO: Stripping punctuation twice in count_words and count_letters try to apply dry principle

def count_frequent_word(text: str) -> Counter[str]:
    """ A data type of Counter with the first element being the word and the second element being the number of times that word appears in the text.

    Example of the return:
        [("the", 4), ("my", 3)]
    """
    text = strip_punctuation(text)
    words = text.split()
    word_counter = Counter(words)
    
    return word_counter.most_common()

def count_sentences(text: str) -> int:
    """ Counts the number of full stop sentences. If there are characters between the period it will not count as a full stop sentence.
    
    Examples: 
    This would. Be considered. 3 sentences.
    This would.Would be considered. 2 sentences.
    
    """
    
    # Remove non full stop punctuations
    text = re.sub(pattern = "\.(?!\s|$)",
                  repl = "",
                  string = text)
    
    return text.count(".")
    
def count_letters(text: str) -> int:
    
    text = strip_punctuation(text)
    
    # Removes spaces from the text so only characters are left
    text = strip_gaps(text)
    text = text.replace(" ", "")
    
    count = 0
    for i in text:
        count += 1
        
    return count

def count_words(text):
    """Counts the number of words in each string. Will ignore punctuation"""
    
    # Remove away the punctuations in the text
    text = strip_punctuation(text)
    
    # Create an array of words
    text = word_tokenize(text)
    
    return len(text)

def extract_text_from_url(url: str):
    
    html = urllib.request.urlopen(url)
    html_parsed = BeautifulSoup(html, 'html.parser')
    
    text = ""
    
    for paragraph in html_parsed.find_all("p"):
        text += paragraph.get_text()
    
    return text
    
def text_summary(text: str, articles: bool = 0, url: bool = 0) -> dict:
    """ Returns a summary of the string including how many words, letters, sentences, letters / word, words / sentence, most frequent word within the block of text including compute time.

    Args:
        text (str): The block of text that is being computed.
        articles (bool): Determines whether to count articles or remove them (0 by default is to include them)
        
    Returns:
        dict: _description_
    """
    
    text_details = {}
    
    if url:
        text = extract_text_from_url(text)
    
    # if articles:
    #     text = "".join(strip_articles(text))
    
    text_details["words"] = count_words(text)
    text_details["letters"] = count_letters(text)
    text_details["sentences"] = count_sentences(text)
    
    try:
        text_details["letters_per_word"] = text_details["letters"] / text_details["words"]
    except ZeroDivisionError:
        text_details["letters_per_word"] = 0
    
    try:
        text_details["words_per_sentence"] = text_details["words"] / text_details["sentences"]
    except ZeroDivisionError:
        text_details["words_per_sentence"] = 0
        
    text_details["most_frequent_word"] = count_frequent_word(text)[0][0]
    
    return text_details

def text_similarity(text1: str, text2: str) -> int:
    return fuzz.token_sort_ratio(text1, text2)

def sentiment_analysis(text: str):
    sentiment_pipeline = pipeline('sentiment-analysis')
    return sentiment_pipeline(text)

if __name__ == '__main__':
    test = """
    Physics is the natural science that studies matter,[a] its fundamental constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, with its main goal being to understand how the universe behaves. A scientist who specializes in the field of physics is called a physicist.
    """
    print(text_summary(test))