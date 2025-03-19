
import sys


def get_book_text(book_path):

    with open(book_path) as f:
        book_text = f.read()

    return book_text



def main():

    #allow user to input name of selected book
    selected_book = sys.argv
    print(sys.argv)

    if len(selected_book) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    #retrieve text of selected book as string
    book_text = get_book_text(selected_book[1])


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {selected_book[1]}")
    print("----------- Word Count ----------")


    #calculate total word count of selected book
    from stats import get_word_count
    word_count = get_word_count(book_text)


    print(f"Found {word_count} total words")
    print("--------- Character Count -------")


    #build list of all characters and their numbers of appearances in selected book
    from stats import get_character_count
    character_count_dictionary = get_character_count(book_text)


    #sort list of characters/appearances from greatest number of appearances to least
    from stats import sorter
    sorted_dictionary = sorter(character_count_dictionary)
    for entry in sorted_dictionary:
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")

    print("============= END ===============")


main()
