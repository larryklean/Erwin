import json


# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename, 'r') as json_obj:
#             username = json.load(json_obj)
#     except FileNotFoundError:
#         username = input('input username：')
#         with open(filename, 'w') as json_obj:
#             json.dump(username, json_obj)
#         print('we will remember you when you come back later %s ' % username)
#     else:
#         print('welcome! %s' % username)


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename, 'r') as json_obj:
            username = json.load(json_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('what\'s your name?')
    filename = 'username.json'
    with open(filename, 'w') as json_write:
        json.dump(username, json_write)


def greet_user():
    username = get_stored_username()
    if username:
        print('Welcome %s' % username)
    else:
        get_new_username()
        print('we will remember you later')

greet_user()
