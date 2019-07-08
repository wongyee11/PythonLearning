#!/usr/bin/env.python
# coding=utf-8

'''
创建一个目录‘project’，并在目录下创建两个文件，结构如下：
project/
|
|--pub.py
|
|--count.py
'''
from pub import add

print(add(1, 8))
print("在相同的目录下再创建一个文件‘count.py’，调用‘pub.py’文件里的‘add()’函数")
print("这样就实现了跨文件的函数调用")