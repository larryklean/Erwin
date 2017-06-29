# 定义类
class Student(object):
    # 类属性
    _grade = "1701"

    def __init__(self, name, age):
        # 实例属性
        self._name = name
        self._age = age

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")

        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100")

        self._score = value

    @property
    def get_score(self):
        return self._score

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    @property
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def print_score(self):
        print("%s：%s" % (self._name, self._age))

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def age(self):
        return 2017 - self._birthday


tom = Student("tom", 18)
print(tom.get_name)
print(Student.age)

# 创建对象
# del Student.grade

# tom = Student("tom", 18)
# tom.print_score()
# print(Student.grade)
#
# print(tom.get_name())
# print(tom.get_age())
