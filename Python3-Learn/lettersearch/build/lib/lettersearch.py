def lettersearch(phrase:str, letters:str) -> set:
    """This module takes a phrase provided by the user and searches it for letters that the user provides"""
    return set(letters).intersection(set(phrase))
