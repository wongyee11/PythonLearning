#!/usr/bin/env.python
# coding=utf-8

print("使用for直接对一个字符串进行遍历")
for i in "hello world":
    print(i)

print("使用for对一个字典进行遍历")
fruits = ['banana','apple','mango']
for fruit in fruits:
    print(fruit)

print("需要进行一定次数的遍历，需要借助range()函数")
for i in range(5):
    print(i)

print("range()默认是从零开始，还可以设置起始位置和步长。例如打印1到10的奇数,range(start,end[,step])")
'''
range(start,end[,step])
range()函数，start表示开始位置，end表示结束位置,step表示每一次的步长。

Python3的range()和Python2的xrange()用法相同，是一个数组。
'''
for i in range(1,10,2):
    print(i)

for i in range(2,11,2):
    print(i)