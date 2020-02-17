import re

password = input()
regexExp = '^' + password.replace('_', '.') + '$'
pattern = re.compile(regexExp, re.MULTILINE)

words = []

with open('slownik_pl.txt') as f:
    for _ in range(7):
        next(f)
    for word in f:
        if pattern.match(word):
            words.append(word)

print('Pasujące słowa to: ' + ' '.join(words))
