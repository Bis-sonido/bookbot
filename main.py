import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    count = get_num_characters(text)
    sorting = sorted_list(count)
    in_order_report(path, num_words, sorting)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def in_order_report(path, num_words, sorting):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorting:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
        

main()