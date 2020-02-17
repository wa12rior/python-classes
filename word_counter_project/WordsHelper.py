"""
Helper module responsible for investigating everything about words in file.
"""

import string


def unique_words(input):
    """
    Function counts unique words in input.

    :param input:
    File name.

    :return output:
    Structure with only unique words from input.
    """

    output = set()

    with open(input) as f:
        for line in f:
            words = format_string(line)
            for word in words:
                output.add(word)

    return output


def words_counter(input):
    """
    Function provides words with number of their encounters.

    :param input:
    File name.

    :return output:
    Dict with words and count.
    """
    output = {}

    with open(input) as f:
        for line in f:
            words = format_string(line)
            for word in words:
                if not output.get(word):
                    output[word] = 1
                else:
                    output[word] += 1

    return output


def format_string(text):
    """
    Gets rid off unwanted chars.

    :param text:
    Input text.

    :return text:
    Properly formatted text.
    """
    unwanted_chars = [',', '.', '[', ']', ':', ')', '(', '*', ';', '@', '#', '?', '!', '&', '$', '\"', '-', '\'']

    for char in unwanted_chars:
        text = text.replace(char, ' ')
    text = text.lower()
    text = text.split()

    for word in text:
        word = word.strip()

    return text
