#!/usr/bin/env.python
# coding=utf-8

print("通常'else'语句只有在没有异常的情况下才会被执行，但有些情况下不管是否出现异常，这些操作都希望被执行")
print("例如文件的关闭、锁的释放、把数据库连接返还给连接池等操作")
print("我们可以使用'try...except...finally'语句来实现这样的需求")
try:
    print(n)
except Exception as m:
    print(m)
finally:
    print("不管是否异常，我都会被执行。")

print("修改代码：")
print("定义'n'变量")
try:
    n = "异常测试："
    print(n)
except Exception as m:
    print(m)
finally:
    print("不管是否异常，我都会被执行。")