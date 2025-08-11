import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
def num_of_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def main():
    file_path = "books/frankenstein.txt"
    contents = get_book_text(file_path)
    word_count = num_of_words(contents)
    print(f"{word_count} words found in the document")


main()
