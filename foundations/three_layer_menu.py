menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

while True:
    for item in menu:
        print(item)
    choice = input(">请选择：")
    if choice in menu:
        while True:
            for item2 in menu[choice]:
                print(item2)
            choice2 = input(">>请选择：")
            if choice2 in menu[choice]:
                while True:
                    for item3 in menu[choice][choice2]:
                        print(item3)
                    choice3 = input(">>>请选择：")
                    if choice3 in menu[choice][choice2]:
                        for item4 in menu[choice][choice2][choice3]:
                            print(item4)
                        choice4 = input("最后一层,按b返回：")
                        if choice4 == "b":
                            continue
                    if choice3 == "b":
                        break
            if choice2 == "b":
                break
    if choice == "b":
        print("退出程序")
        exit(0)
