class Animal(object):
    def run(self):
        print("Animal is running...")


class Cat(Animal):
    pass


# python中不一定需要发生继承关系 才能实现多带 只要子类
class Dog(object):
    def run(self):
        print("Dog is running...")


def run_twice(animal):
    animal.run()
    animal.run()


cat = Cat()
# cat.run()

dog = Dog()
# dog.run()


run_twice(Dog())
