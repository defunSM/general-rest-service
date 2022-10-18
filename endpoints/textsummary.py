""" Endpoint which summarizes the numerical amount of words, sentences, letters in a given text."""

from src.countleaf.helpers import count_frequent_word, count_sentences, count_letters, count_words, extract_text_from_url


def text_summary(text: str, articles: bool = 0, url: bool = 0) -> dict:
    """Returns a summary of the string including how many words, letters, sentences, letters / word,
    words / sentence, most frequent word within the block of text including compute time.

    Args:
        text (str): The block of text that is being computed.
        articles (bool): Count articles or remove them (0 by default is to include them)

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
        text_details["letters_per_word"] = (
            text_details["letters"] / text_details["words"]
        )
    except ZeroDivisionError:
        text_details["letters_per_word"] = 0

    try:
        text_details["words_per_sentence"] = (
            text_details["words"] / text_details["sentences"]
        )
    except ZeroDivisionError:
        text_details["words_per_sentence"] = 0

    text_details["most_frequent_word"] = count_frequent_word(text)[0][0]

    return text_details
