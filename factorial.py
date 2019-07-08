#!/usr/bin/env.python
# coding=utf-8

#阶乘公式：n! = n*(n-1)!
def f1(n):
    c = 1
    for i in range(n):
        i = i + 1
        c = c * i
    return c #c的值是上一次计算的数值,i=n-1+1,4*(3*(2*1))*1*1

print(f1(4))

def f2(n):
    if n > 1:
        return n*f2(n-1) #n乘以上一次运算的值，4*f2(3)=4*(3*f2(2))*(2*f2(2))*1*1)
    else:
        return 1

print(f2(4))