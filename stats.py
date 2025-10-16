def get_sys_argv_book_name(argv):
    return argv[1]

def sort_chars_map(chars_map):
    return {k: v for k, v in sorted(chars_map.items(), key=lambda item: item[1], reverse=True)}

def count_words(content):
    count = 0
    for w in content.split():
        if (len(w) > 0):
            count += 1
    return count

def count_chars(content):
    chars_map = {}
    for i in range(0, len(content)):
        char = content[i].lower()
        if (not char in chars_map):
            chars_map[char] = 0
        chars_map[char] += 1
    return chars_map

def print_report(book_path, words_count, chars_map):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char in chars_map:
        if (char.isalpha()):
            print(f"{char}: {chars_map[char]}")
    print("============= END ===============")
