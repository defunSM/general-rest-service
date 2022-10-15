""" Helper functions for Countleaf. """

# pylint: disable=[anomalous-backslash-in-string]

import re
import urllib.request
from collections import Counter
from typing import List

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def strip_punctuation(text: str) -> str:
    """Removes any punctuations from text and returns the punctuation free text.

    Args:
        text (str): text that needs to be stripped of punctuation.

    Returns:
        str: text that does not have any punctuation.
    """

    stripped_text = re.sub(pattern="[^\w\s]", repl="", string=text)

    return stripped_text


def strip_gaps(text: str) -> str:
    """Replaces all tabs and newlines (gaps) in text to a single space."""

    new_text = re.sub(pattern="[\t\n]", repl="", string=text)

    return new_text


def strip_articles(tokenized_words: List[str]) -> str:
    """Use nltk's stopwords corpus to filter out articles from text."""

    text_without_articles = [
        word for word in tokenized_words if not word in stopwords.words()
    ]

    return text_without_articles


def count_frequent_word(text: str) -> Counter[str]:
    """A data type of Counter with the first element being the word and the second element being
    the number of times that word appears in the text.

    Example of the return:
        [("the", 4), ("my", 3)]
    """
    text = strip_punctuation(text)
    words = text.split()
    word_counter = Counter(words)

    return word_counter.most_common()


def count_sentences(text: str) -> int:
    """Counts the number of full stop sentences.
    If there are characters between the period it will not count as a full stop sentence.

    Examples:
    This would. Be considered. 3 sentences.
    This would.Would be considered. 2 sentences.

    """

    # Remove non full stop punctuations
    text = re.sub(pattern="\.(?!\s|$)", repl="", string=text)

    return text.count(".")


def count_letters(text: str) -> int:
    """ Returns the number of letters in the text as an integer value.

    Args:
        text (str): A non empty text containing alphanumeric characters.

    Returns:
        int: A non zero integer representing the number of letters in the text.
    """

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


def extract_text_from_url(url: str) -> str:
    """ Strips all html tags from the url and only returns the text.

    Args:
        url (str): A valid https or http link.

    Returns:
        text (str): A string of all the text on the url.
    """

    html = urllib.request.urlopen(url)
    html_parsed = BeautifulSoup(html, "html.parser")

    text = ""

    for paragraph in html_parsed.find_all("p"):
        text += paragraph.get_text()

    return text
