#import os
#print(os.getcwd())
import sys
from stats import count_words
from stats import count_chars
from stats import convert_dict_to_list

#print(f' The path is {sys.argv[0]}')

def get_book_text(file_path):
    with open (file_path) as file:
        file_contents= file.read()
    return file_contents

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path=sys.argv[1]
    file_contents=get_book_text(file_path)
    count_chars_dict ={}
    #print(file_contents)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    count_words(file_contents)
    print("--------- Character Count -------")
    count_chars_dict=count_chars(file_contents)
    convert_dict_to_list(count_chars_dict)
    print("============= END ===============")
    return 0

main()

