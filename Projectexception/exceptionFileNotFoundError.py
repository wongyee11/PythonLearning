#!/usr/bin/env.python
# coding=utf-8

print("'Python'用一场对象('exception object')来表示异常情况")
print("遇到错误后，会引发异常，如果异常对象并未被处理或捕捉，则程序就会用所谓的回溯('Traceback',一种错误信息)来中止执行")
print("我们通过'oper()'方法以读"r"的方式打开一个'abc.txt'的文件")
print("然后'Python'抛出一个'FileNotFoundError'类型的异常")
print("它告诉我们:'No such file or directory: 'abc.txt''(没有'abc.txt'这样的文件或目录)")
print("我们根本就没创建这个文件")
print("我们可以通过'Python'所提供的'try...except...'语句来接受并处理这个异常")
#open("abc.txt", 'r') #'open()'一个根本不存在的文件时会抛'FileNotFoundError'异常

#我们可以通过'Python'所提供的'try...except...'语句来接受并处理这个异常
try:
    open("abc.txt",'r')
except FileNotFoundError:
    print("输出结果：")
    print("异常了（exception）!")