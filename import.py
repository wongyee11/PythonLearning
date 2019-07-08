#!/usr/bin/env.python
# coding=utf-8

print("模组更通俗地叫‘类库’或‘模块’")
print("如果想实现与时间有关的功能，就需要调用系统的‘time’模块")
print("如果想实现与文件和文件夹有关的操作，就需要用到‘os’模块")
print("例如我们通过‘Selenium’实现的‘Web’自动化测试，那么‘Selenium’对于‘Python’来说就是一个第三方扩展模块")

print("在‘Python’里，通过‘import...’或‘from...import...’的方式引用模块")
print("下面引用‘time’模块")
import time
print(time.ctime())

print("在‘time’模块下面有一个‘ctime()’方法用于获得当前时间，通过‘print()’将当前时间打印出来")
print("如果确定了只会用到‘time’下面的‘ctime’方法，可以这样引入")
from time import ctime

print("现在使用时就不必告诉‘Python’，‘ctime()’是‘time’模块所提供的了")
print(ctime())

print("有时候我们可能还会用到‘time’模块下面的‘sleep()’休眠方法，当然我们也可以吧'sleep()'方法引入进来")
print("或许还会用到其他方法，这是可以一次性把'time'模块下的所有方法都引入进来")
print("星号‘*’用于表示模块下面的所有方法")
print("‘time’是‘Python’语言提供的核心方法，而且经过了编译,所以我们无法看到‘ctime’是如何取到系统的当前时间的")
from time import *

print(ctime())
print("休眠两秒")
sleep(2)
print(ctime())

print("我们可以通过‘help()’方法查看‘time’的帮助说明")
import time
help(time)

print("‘pip’所安装的‘Python’的第三方类库或框架可以查看其类方法的实现，例如我们做‘Selenium’类库")
print("‘Python’所安装的第三方类库或框架模块存放在‘..\PythonXX\Lib\site-packages\目录下面，已经安装的'Selenium’就在这个目录下面")
import selenium
help(selenium)