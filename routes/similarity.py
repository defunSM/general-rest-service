from thefuzz import fuzz


def text_similarity_score(text1: str, text2: str) -> int:
    return fuzz.token_sort_ratio(text1, text2)
