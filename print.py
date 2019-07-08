#!/usr/bin/env.python
# coding=utf-8

print("Hello Python")

print("%s(string)只能打印字符串")
name = "zhangsan"

print("Hello %s,Nice to meet you!" %name)

name = "lisi"

print("Hello %s,Nice to meet you!" %name)

print("%d(date)只能打印数字")
age = 27
print("You are %d !" %age)

print("%r(不知类型信息)不知道打印的是什么类型的信息使用")
n = 100
print("You print is %r ." %n)

n = "abc"
print("You print is %r" %n)

name = "Hello"
age = 19
print("人物信息 ： %s %d ." %(name,age))