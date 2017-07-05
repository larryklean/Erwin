_username = "admin"
_password = "123"

username = input("username:")
password = input("password:")

if username == _username and password == _password:
    print("Welcome user {name}...".format(name=username))
else:
    print("Invalid username or password")
