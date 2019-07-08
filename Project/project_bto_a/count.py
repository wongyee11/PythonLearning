#!/usr/bin/env.python
# coding=utf-8

'''
创建一个目录‘project’，并在目录下创建另一个目录‘model’，在这个目录下创建一个文件，另一个文件在‘project’目录下，结构如下：
project/
|
|--model
|   |
|   |--pub.py
|
|--count.py
'''
from model.pub import add

print(add(1, 8))
print("创建一个目录‘project’，并在目录下创建另一个目录‘model’，在这个目录下创建一个文件，另一个文件在‘project’目录下")
print("使用‘model.pub‘’(模块名称).(方法名称)’这样就实现了跨目录文件的函数调用")
#‘Python2’里将会抛出ImportError：找不到名字为‘model’的模块