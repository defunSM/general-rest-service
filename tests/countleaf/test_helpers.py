""" Pytest for helpers.py"""

# pylint: disable=[missing-function-docstring line-too-long]


from src.countleaf.helpers import strip_punctuation

TEXT = """A dream, all a dream, that ends in nothing, and leaves the sleeper where he lay down, but I wish you to know that you inspired it."""

def test_strip_punctuation():
    expected_text = """A dream all a dream that ends in nothing and leaves the sleeper where he lay down but I wish you to know that you inspired it"""
    assert strip_punctuation(TEXT) == expected_text

def test_strip_gaps():
    pass

def test_strip_articles():
    pass

def test_count_frequent_word():
    pass

def test_count_sentences():
    pass

def test_count_letters():
    pass

def test_count_words():
    pass

def test_extract_text_from_url():
    pass