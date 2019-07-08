#!/usr/bin/env.python
# coding=utf-8

print("Python里通过def关键字来定义'函数'")
print("创建一个add()函数，此函数接收两个参数a、b")
def add(a, b):
    print(a + b)
print("传两个参数3、5给add()函数")
add(1, 8)

print("通常add()函数不会直接打印结果，而是将处理结果通过return关键字返回")
def add(a, b):
    #return a + b #在Terminal里可使用return a + b
    print(a + b)
add(1, 8)

print("有时不想传参，可以为add()函数设置默认参数")
def add(a=1, b=8):
    #return a + b #在Terminal里可使用return a + b
    print(a + b)

print("不传参数给add()，函数使用默认参数进行计算")
add()

print("传参数给add()，函数则计算参数的值")
add(1, 8)