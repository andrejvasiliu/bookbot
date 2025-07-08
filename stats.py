def count_words(text: str) -> int:
    count = len(text.split())

    return count

def char_count(text: str) -> dict[str, int]:
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts