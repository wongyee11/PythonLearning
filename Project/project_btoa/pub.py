#!/usr/bin/env.python
# coding=utf-8

print("‘模块调用’，自己创建一个模块，然后通过另一个程序调用")
print("对于一个软件项目来说不会把所有代码都放在一个文件里实现，它们一般会按照一定规则在不同的目录和文件里实现")
print("‘project’=》pub.py、count.py")
'''
创建一个目录‘project’，并在目录下创建两个文件，结构如下：
project/
|
|--pub.py
|
|--count.py
'''
print("创建‘add’函数")
def add(a, b):
    return a + b