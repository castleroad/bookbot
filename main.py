from sys import argv
from stats import *

def get_book_content(path):
    with open(path) as book:
        content = book.read()
    return content

def main():
    if (len(argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = get_sys_argv_book_name(argv)

    content = get_book_content(path)
    words_count = count_words(content)
    chars_map = count_chars(content)

    print_report(path, words_count, sort_chars_map(chars_map))

main()
