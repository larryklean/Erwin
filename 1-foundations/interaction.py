# username = input("username:")
# password = input("password:")
# print("username：" + username + "   password：" + password)

# raw_input of 2.x equals input 3.x
# don't use
name = input("name：")
# age = int(input("age："))
age = input("age：")
print(type(age))
job = input("job：")
salary = input("salary：")

info = '''
---- info of %s ----
name：%s
age：%s
job：%s
salary：%s
''' % (name, name, age, job, salary)

info2 = '''
---- info2 of {_name} ----
name：{_name}
age：{_age}
job：{_job}
salary：{_salary}
'''.format(_name=name, _age=age, _job=job, _salary=salary)

info3 = '''
---- info3 of {0} ----
name：{0}
age：{1}
job：{2}
salary：{3}
'''.format(name, name, age, job, salary)

print(info3)
