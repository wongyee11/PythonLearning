#!/usr/bin/env.python
# coding=utf-8
print("‘if和else语句进行分支判断’")
a = 2
b = 3
if a > b:
    print("a max")
else:
    print("b max")

print("‘==’运算符判断‘相等’")
student = "xiaoming"
if student == "xiaoming":
    print("xiaoming, You are on duty today")
else:
    print("Please call xiaoming to duty")

print("‘！=’运算符判断‘不相等’")
student = "xiaoming"
if student != "xiaoming":
    print("Please call xiaoming to duty")
else:
    print("xiaoming, You are on duty today")

print("‘in和not in’表示'包含的关系")
hi = "hello world"
if "hello" in hi:
    print("Contain")
else:
    print("Not Contain")

if "hello" not in hi:
    print("Not Contain")
else:
    print("Contain")

print("if 可以进行布尔类型的判断")
a = True
b = False
if a:
    print("a is True")
else:
    print("a is not True")
if b:
    print("b is True")
else:
    print("b is not True")

print("'if...elif...else'进行多重条件判断")
'''
Traceback (most recent call last):
  File "G:/PycharmProjects/PythonLeaning/if.py", line 55, in <module>
    if results >= 90:
TypeError: '>=' not supported between instances of 'str' and 'int'

这是因为input()返回的数据类型是str，不能直接和整数进行比较，必须先把str换成整数，使用int()方法：

results = input("请输入成绩：")
results = int(results)
或者
n = input('results')
results = int(n)
'''
n = input("请输入成绩：")
results = int(n)

#results = 91

if results >= 90:
    print('优秀')
elif results >= 70:
    print('良好')
elif results >= 60:
    print('及格')
else:
    print('不及格')