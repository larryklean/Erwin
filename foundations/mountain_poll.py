responses = {}

polling_active = True

while polling_active:
    name = input("please input your name: ")
    response = input("which mountain would you like to climb someday?: ")

    responses[name] = response

    repeat = input("would you want to let another person respond?")

    if repeat == 'no':
        break
for name, mountain in responses.items():
    print("name：%s\t response：%s" % (name, mountain))

# delete someone
# for name in responses.keys():
#     if name == 'bob':
#         responses.pop(name)

keys = list(responses.keys())
# for key in keys:
#     del responses[key]

print(type(keys))
for name, mountain in responses.items():
    print("name：%s\t response：%s" % (name, mountain))
