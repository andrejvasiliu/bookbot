from stats import count_words, char_count

def get_book_text(path: str) -> str:
    content = None
    with open(path) as f:
        content = f.read()

    return content

def main():
    frankenstein_path = "./books/frankenstein.txt"
    content = get_book_text(frankenstein_path)

    word_count = count_words(content)
    print(f"{word_count} words found in the document")

    char_ccount = char_count(content)
    print(char_ccount)

main()