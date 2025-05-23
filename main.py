from stats import get_num_words, get_char_count, get_sorted_dicts
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def report(path_to_file):
    book_text = get_book_text(path_to_file)
    char_count = get_char_count(book_text)
    sorted_dicts = get_sorted_dicts(char_count)
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_dict in sorted_dicts:
        if sorted_dict["char"].isalpha():
            print(f"{sorted_dict['char']}: {sorted_dict['num']}")
    print("============= END ===============") 



def main():
    if len(sys.argv) == 2:
        report(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
    
