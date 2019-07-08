#!/usr/bin/env.python
# coding=utf-8

print("从'Python2.5'版本之后，所有的异常类都有了新的基类'BaseException'")
print("这‘Exception’类也继承了'BaseException'，所以我们也可以使用'BaseException'来接收所有类型的异常")
try:
    open("abc.txt",'r')
    print(hello)
except BaseException:
    print("异常了！")