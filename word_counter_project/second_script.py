import WordsHelper
from itertools import islice


def most_common(input, n):
    """
    Function gives most common encounters of word.

    :param n:
    First n results of words.
    :param input:
    Return from function word_counter() in module WordsHelper.
    :return output:
    Returns list with tuple pairs of word and count of it
    """
    output = {k: v for k, v in sorted(input.items(), key=lambda item: item[1], reverse=True)}
    return list(islice(output.items(), n))


rows = 10

HAMLET_DICT_WORDS = WordsHelper.words_counter('hamlet.txt')
MAKBET_DICT_WORDS = WordsHelper.words_counter('makbet.txt')
OTELLO_DICT_WORDS = WordsHelper.words_counter('otello.txt')

works = [
    (most_common(HAMLET_DICT_WORDS, rows), 'Hamlet: '),
    (most_common(MAKBET_DICT_WORDS, rows), 'Makbet: '),
    (most_common(OTELLO_DICT_WORDS, rows), 'Otello: '),
]

for work in works:
    print('\n')
    print(work[1], '\n')
    print('lp.   |    wyraz   |    wystapienia')
    for row in range(rows):
        print(row + 1, '   |    ', work[0][row][0], '   |   ', work[0][row][1])
