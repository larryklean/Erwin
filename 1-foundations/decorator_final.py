username = "john"
password = "123"


# auth decoration
def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            _username = input("input name:")
            _password = input("input password:")
            if auth_type == "local":
                if _username == username and _password == password:
                    print("user has passed!")
                    res = func(*args, **kwargs)
                    if res is not None:
                        return res
                else:
                    exit("invalid username or password")
            else:
                print("remote do not work")

        return wrapper

    return outer_wrapper


@auth(auth_type="local")
def home():
    print("welcome to home")


@auth(auth_type="remote")
def bbs():
    print("welcome to bbs")


# home()

bbs()
