import WordsHelper
import collections, functools, operator


def common_pairs(first_dict, second_dict):
    """
    Merge two dicts with common pairs.

    :param first_dict:
    First dict.
    :param second_dict:
    Second dict.
    """
    ini_dict = [first_dict, second_dict]
    result = dict(functools.reduce(operator.add, map(collections.Counter, ini_dict)))

    print("Resultant dictionary : ", str(result))


# 1.
HAMLET_SET_WORDS = WordsHelper.unique_words('hamlet.txt')
HAMLET_DICT_WORDS = WordsHelper.words_counter('hamlet.txt')

MAKBET_SET_WORDS = WordsHelper.unique_words('makbet.txt')
MAKBET_DICT_WORDS = WordsHelper.words_counter('makbet.txt')

OTELLO_SET_WORDS = WordsHelper.unique_words('otello.txt')
OTELLO_DICT_WORDS = WordsHelper.words_counter('otello.txt')

# 2.
print('Unique words in each text:')
print('Hamlet: ', len(HAMLET_SET_WORDS))
print('Makbet: ', len(MAKBET_SET_WORDS))
print('Otello: ', len(OTELLO_SET_WORDS))

HAMLET_WORD_COUNT = 0
MAKBET_WORD_COUNT = 0
OTELLO_WORD_COUNT = 0

for count in HAMLET_DICT_WORDS:
    HAMLET_WORD_COUNT += HAMLET_DICT_WORDS[count]
for count in MAKBET_DICT_WORDS:
    MAKBET_WORD_COUNT += MAKBET_DICT_WORDS[count]
for count in OTELLO_DICT_WORDS:
    OTELLO_WORD_COUNT += OTELLO_DICT_WORDS[count]

print('All words in each text:')
print('Hamlet: ', HAMLET_WORD_COUNT)
print('Makbet: ', MAKBET_WORD_COUNT)
print('Otello: ', OTELLO_WORD_COUNT)

# 3.
print('Common pairs for works.')
common_pairs(HAMLET_DICT_WORDS, MAKBET_DICT_WORDS)
common_pairs(HAMLET_DICT_WORDS, OTELLO_DICT_WORDS)
common_pairs(MAKBET_DICT_WORDS, OTELLO_DICT_WORDS)
