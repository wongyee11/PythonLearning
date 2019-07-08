#!/usr/bin/env.python
# coding=utf-8

print("在'Python'里所有的异常类都继承'Exception'，所以可以使用它来接收所有类型的异常")

try:
    open("abc.txt", 'r')
except Exception:
    print("异常了！")