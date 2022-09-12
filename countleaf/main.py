
import re

def count_sentences(text: str) -> str:
    """ Counts the sentences based on how many periods there are after a alpha
    """

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
    """ Replaces all tabs and newlines (gaps) in text to a single space"""
    
    new_text = re.sub(pattern = '[\t\n]', 
                      repl = '',
                      string = text)
    
    return new_text

def count_words(text):
    """Counts the number of words in each string. Will ignore punctuation"""

def text_summary(text: str) -> dict:
    """ Returns a summary of the string including how many words, letters, sentences, letters / word, words / sentence, most frequent word and compute time.

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