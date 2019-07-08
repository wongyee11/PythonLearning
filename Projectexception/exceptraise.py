#!/usr/bin/env.python
# coding=utf-8

print("'print()'方法只能打印错误信息，'Python'里提供了'raise'方法来抛出一个异常信息")
from random import randint

#生成一个1到9之间的随机数
number = randint(1, 9)

# 'raise'只能使用'Python'里所提供的异常类，如果自定义一个'abcError'的异常，则'Python'会告诉你'abcError'没有定义
if number % 2 == 0:
    raise NameError("%d is even" % number)
else:
    raise NameError("%d is odd" % number)


'''
try:
    try:
        raise Exception   #open("abc.txt", 'r')
    except Exception:
        print ("inner exception")   #首先被内层Exception异常捕获，打印“inner exception”
        raise   # <same as raise Exception>
except Exception:
    print ("outter exception")  #然后把相同的异常再抛出，被外层的except捕获，打印"outter exception"

try:
  do something
except Exception:  
  raise
#这个是把最近一次产生的异常重新抛出来，交给上层处理。（我已经知道这个异常发生并且捕获到了，但是我不做处理，而由我的上层调用处理。）
'''