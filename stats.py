def count_words(text):
    text_list = text.split()
    num_words = len(text_list)
    return num_words

def count_char(text):
    char_number = {}
    lowered = text.lower()
    for char in lowered:
        if char in char_number:
            char_number[char] += 1
        else:
            char_number[char] = 1
    return char_number

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    char_count = []
    for char in dict:
        char_dict = {"char": char, "num": dict[char]}
        char_count.append(char_dict)
    char_count.sort(reverse=True, key=sort_on)
    return char_count
