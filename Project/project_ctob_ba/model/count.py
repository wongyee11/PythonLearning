#!/usr/bin/env.python
# coding=utf-8

print("多个文件跨目录模块调用")
'''
project
|--model（模组、类库、模块）
|   |
|   |--count.py（模组、类库、模块，A是这个模块下的一个类）
|   |
|   |--new_count.py（模组、类库、模块，B是这个模块下的一个类）
|
|--test.py（调用程序）
'''
#在‘count‘模块下创建类‘A’
class A():

    # 给‘A’这个类创建add()方法，第一个参数必须存在的，习惯命名为‘self’，调用这个方法的时候不需要为这个参数传值
    def add(self, a, b):
        return a + b

print("‘Python2’还需要在‘.../model/目录下创建一个__init__.py文件，用来标识这是一个标准的包含了‘Python’模块的目录’")