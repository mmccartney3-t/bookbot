def num_of_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def num_of_characters(file_contents):
    lower_file_contents = file_contents.lower()
    characters = {}
    for i in lower_file_contents:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

def sort_on(item):
    return item["num"]

def sort_dict(characters):
    characters_list = [{"char": k, "num": v} for k, v in characters.items()]
    characters_list.sort(key=sort_on, reverse=True)
    return characters_list