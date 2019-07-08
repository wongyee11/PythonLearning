#!/usr/bin/env.python
# coding=utf-8

print("打印一个没有定义的变量")

#使用错误的接收异常类型
try:
    print(hello)
except FileNotFoundError:
    print("异常了！")

'''
try:
    print(hello)
except NameError:
    print("这是一个'name'异常！")
'''