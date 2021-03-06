#! \usr\bin\env python3

# Replaces all ADJECTIVE, NOUN, ADVERB, VERB keywords with user input in text.

import os
import re


def replace_words():
    if not os.path.exists('madlibs.txt'):
        print('路径不存在')
        return
    with open('madlibs.txt', 'r', encoding='utf-8') as madlibs_file:
        adjective_regex = re.compile(r'^ADJECTIVE')
        noun_regex = re.compile(r'^NOUN')
        adverb_regex = re.compile(r'^ADVERB')
        verb_regex = re.compile(r'^VERB')
        # 将文件中的字符串以空格切分为数组
        words = madlibs_file.read().split(' ')
        # 遍历数组进行正则匹配并替换
        for index in range(len(words)):
            if adjective_regex.match(words[index]):
                replace_word = adjective_regex.sub(input('请输入：\n'), words[index])
            elif noun_regex.match(words[index]):
                replace_word = noun_regex.sub(input('请输入：\n'), words[index])
            elif adverb_regex.match(words[index]):
                replace_word = adverb_regex.sub(input('请输入：\n'), words[index])
            elif verb_regex.match(words[index]):
                replace_word = verb_regex.sub(input('请输入：\n'), words[index])
            else:
                continue
            words[index] = replace_word
        with open('madlibs_duplicate.txt', 'w', encoding='utf-8') as madlibs_duplicate_file:
            mad_str = ' '.join(words)
            madlibs_duplicate_file.write(mad_str)


replace_words()
