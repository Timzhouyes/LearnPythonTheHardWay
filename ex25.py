def break_words(stuff):
    """Here is document of this function"""
    words = stuff.split(' ')
    return words


def sort_word(words):
    return sorted(words)


def print_first_word(words):
    word = words.pop(0)
    return word


def print_last_word(words):
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    words = break_words(sentence)
    word = sort_word(words)
    return word


def print_first_and_last(sentence):
    words = break_words(sentence)
    first = print_first_word(words)
    last = print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
