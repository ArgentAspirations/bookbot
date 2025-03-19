def get_word_count(book_text):
    word_count = 0

    for word in book_text.split():
        word_count += 1
    
    return word_count



def get_character_count(book_text):
    book_text = book_text.lower()
    
    count_dictionary = {}


    for character in book_text:
        if character not in count_dictionary:
            count_dictionary[character] = 1
        else:
            count_dictionary[character] += 1

    return count_dictionary



def sorter(count_dictionary):
    split_dictionary = []

    for character, count in count_dictionary.items():
        split_dictionary.append({"character": character, "count":count})

    from operator import itemgetter
    split_dictionary.sort(reverse=True, key=itemgetter("count"))
    
    return split_dictionary