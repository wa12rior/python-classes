from random import shuffle, choice

TEST_NUMBER = 4

HEADER = '''Imię i nazwisko:

Data:

Semestr:
'''

QUESTION = '''
{}. Jaką stolicę ma państwo {}?
'''

TITLE = '''
Stolice - sprawdzian (Formularz - {})
'''

ANSWER = '''
A.{}
B.{}
C.{}
D.{}
'''

data = {}

with open('stolice.txt') as f:
    for line in f:
        pair = line.replace('\n', '').split(',')
        data[pair[0]] = pair[1]

countries = [x[0] for x in data.items()]

for test in range(TEST_NUMBER):
    test_file = open('spr{}.txt'.format(test + 1), 'w')
    answer_file = open('odp{}.txt'.format(test + 1), 'w')
    test_file.write(HEADER)
    test_file.write(TITLE.format(test + 1))
    shuffle(countries)

    for question in enumerate(countries):
        question_index = question[0] + 1

        correct_answer = [data[question[1]]]
        incorrect_answers = [
            choice(
                [data[incorrect] for incorrect in data if incorrect != correct_answer]
            ) for incorrect_answer in range(3)
        ]

        answers = correct_answer + incorrect_answers
        shuffle(answers)
        test_file.write(QUESTION.format(question_index, question[1]))
        test_file.write(ANSWER.format(*answers))

        key_answer = str(question_index) + '. '
        if answers.index(correct_answer[0]) == 0:
            key_answer += 'A\n'
        if answers.index(correct_answer[0]) == 1:
            key_answer += 'B\n'
        if answers.index(correct_answer[0]) == 2:
            key_answer += 'C\n'
        if answers.index(correct_answer[0]) == 3:
            key_answer += 'D\n'

        answer_file.write(key_answer)
    answer_file.close()
    test_file.close()
