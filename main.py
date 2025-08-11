def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_path = input("What is the file path\n")
    contents = get_book_text(file_path)
    print(contents)

main()
