import sys

from stats import num_of_words
from stats import num_of_characters
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        contents = get_book_text(file_path)
        word_count = num_of_words(contents)
        character_count = num_of_characters(contents)
        sorted_count = sort_dict(character_count)
        print_report(file_path, word_count, sorted_count)

main()
