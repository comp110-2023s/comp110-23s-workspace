def short_words(given: list[str]) -> list[str]:
    """Returns list of words thta are shorter than 5 characters"""
    new_list: list[str] = []
    for word in given:
        if len(word) >= 5:
            print(f"{word} is too long!")
        else:
            new_list.append(word) 
    return (new_list)