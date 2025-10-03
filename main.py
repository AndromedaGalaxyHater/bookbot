from stats import count_words
from stats import count_char
from stats import sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_num = count_char(text)
    dict_list = sort_dict(char_num)
    print (sys.argv)

    print(f"""============ BOOKBOT ============ 
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    for dict in dict_list:
        if dict["char"].isalpha():
            print (f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============") 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()