import os


# 获取数据字典
def make_capitals():
    # 创建保存答案的字典
    capitals = {}
    # 创建存放试卷文件夹
    if not os.path.exists('tests'):
        os.mkdir('tests')
    with open('text.txt', 'r', encoding='utf-8') as capitals_file:
        for line in capitals_file.readlines():
            text = line.replace('\n', '').split('：')
            capitals[text[0]] = text[1]
    return capitals


# 循环创建35份试卷
def maek_quizs(capitals):
    if not len(os.listdir(os.path.abspath('tests'))) == 35:
        # 判断试卷是否存在
        for num in range(35):
            with open('tests/capitals_quiz%s.txt' % (num + 1), 'w', encoding='utf-8') as quiz_file:
                quiz_file.write('姓名:\n\n时间:\n\n')
                quiz_file.write('试卷(来自 %s)' % (num + 1))
                quiz_file.write('\n\n')
                # 获取所有问题
                states = list(capitals.keys())
    #           打乱问题顺序

    else:
        print("试卷已经存在")


captials = make_capitals()
maek_quizs()
