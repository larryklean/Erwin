import os
import random


def format_capitals(path_name):
    text = {}
    with open(path_name, 'r', encoding='utf-8') as source_file:
        for line in source_file.readlines():
            split_line = line.replace('\n', '').split('：')
            text[split_line[0]] = split_line[1]
    return text


def make_quizs(source):
    if not os.path.exists('tests'):
        os.mkdir('tests')
    for quiz_num in range(35):
        quiz_file = open('tests/capital_quiz_%s.txt' % (quiz_num + 1), 'w', encoding='utf-8')
        answer_file = open('tests/quiz_answer_%s.txt' % (quiz_num + 1), 'w', encoding='utf-8')
        states = list(source.keys())
        random.shuffle(states)
        quiz_file.write('姓名:\n\n时间:\n\n试卷种类:%s\n\n' % (quiz_num + 1))
        for question_num in range(len(source.keys())):
            corret_answer = source[states[question_num]]
            wrong_answer = list(source.values())
            del wrong_answer[wrong_answer.index(corret_answer)]
            wrong_answer = random.sample(wrong_answer, 3)
            answer_options = wrong_answer + [corret_answer]
            random.shuffle(answer_options)
            quiz_file.write('%s.%s的省会是哪里？\n' % (question_num + 1, states[question_num]))
            for i in range(4):
                quiz_file.write('%s. %s\n' % ('ABCD'[i], answer_options[i]))
            quiz_file.write('\n')
            answer_file.write('%s. %s\n' % (question_num + 1, 'ABCD'[answer_options.index(corret_answer)]))
        quiz_file.close()
        answer_file.close()


capitals = format_capitals('source.txt')
make_quizs(capitals)
