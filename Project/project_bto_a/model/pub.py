#!/usr/bin/env.python
# coding=utf-8

print("‘跨目录模块调用’，自己创建一个模块，然后通过另一个程序调用")
print("调用文件与被调用文件不在同一目录下")
print("‘project’=》model-pub.py，count.py")
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
print("创建‘add’函数")
def add(a, b):
    return a + b