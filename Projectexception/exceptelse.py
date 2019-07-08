#!/usr/bin/env.python
# coding=utf-8

print("异常的进阶用法：'try...except...else'")
print("我们对'n'变量进行了赋值，所以没有异常将会执行'else'语句后面的内容")
print("通常'else'语句只有在没有异常的情况下才会被执行")
try:
    n = "异常测试："
    print(n)
except Exception as msg:
    print(msg)
else:
    print("没有异常！")