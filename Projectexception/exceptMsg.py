#!/usr/bin/env.python
# coding=utf-8

print("只要有一行出现了异常就会'print()'异常信息，但是当打印异常时，我们并不能准确地知道到底是哪一行代码引起了异常")
print("我们在'BaseException'后面定义了'msg'变量用于接受异常信息，并通过'print'将其打印出来")
print("此处的写法在'Python2'里用逗号','代替'as'")
try:
    open("abc.txt", 'r')
    print(hello)
except BaseException as msg:
    print(msg)