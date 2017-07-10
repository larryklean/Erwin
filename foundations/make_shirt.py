def make_shirt(size=32, paint="Hello"):
    print("the size of T-shirt is %s and the paint of T-shirt is %s" % (size, paint))


make_shirt(33, 'world！')
make_shirt()
make_shirt(size=55)


####################################################################################################

def get_format_name(first_name, last_name, middle_name=None):
    if middle_name is not None:
        print("full name is %s %s %s" % (first_name, middle_name, last_name))
    else:
        print("full name is %s %s" % (first_name, last_name))


# get_format_name('tom', 'jerry')
# get_format_name('tom', 'jerry', 'tony')

# name = ''
# if len(name):
#     print('ok')
# else:
#     print('not ok')

####################################################################################################

def make_album(singer, title, size=None):
    album = {'singer': singer, 'title': title}
    if size is not None:
        album['size'] = size
    return album


for key, value in make_album('张学友', '吻别', 13).items():
    print("key: %s\t value: %s" % (key, value))

####################################################################################################

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print("current model is %s" % current_model)
        completed_models.append(current_model)


def show_models():
    global completed_models
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_models()


####################################################################################################
# make_pizza
def make_pizza(size, *toppings):
    print('making a %s' % str(size))
    for topping in toppings:
        print(topping)


make_pizza(16, 'peperoni')
make_pizza(12, 'mushroom', 'green pepers', 'extra cheese')


####################################################################################################
# user_profile

def use_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    for k, v in user_info.items():
        profile[k] = v
    return profile


for k, v in use_profile('albert', 'einstein', location='princeton', field='physics').items():
    print('key is %s and value is %s' % (k, v))
