def count_words(text: str) -> int:
    count = len(text.split())

    return count

def sort_char_dict(char_dict: dict) -> dict:
    sorted_char_dicts = []
    for item in char_dict:
        sorted_char_dicts.append({"name": item, "num": char_dict[item]})
        
    sorted_char_dicts.sort(reverse=True, key=lambda item: item["num"])

    return sorted_char_dicts

def char_count(text: str) -> dict:
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict