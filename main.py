from stats import count_words, char_count, sort_char_dict

def get_book_text(path: str) -> str:
    content = None
    with open(path) as f:
        content = f.read()

    return content

def print_report(path: str, word_count: int, sorted_char_dict: list) -> None:
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for item in sorted_char_dict:
        if item["name"].isalpha():
            print(item["name"] + ": " + str(item["num"]))
    print("============= END ===============")

def main():
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    word_count = count_words(content)

    char_dict = char_count(content)
    sorted_char_dict = sort_char_dict(char_dict)

    print_report(path, word_count, sorted_char_dict)

main()