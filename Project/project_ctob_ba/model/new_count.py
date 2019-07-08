#!/usr/bin/env.python
# coding=utf-8

'''
project
|--model（模组、类库、模块）
|   |
|   |--count.py（模组、类库、模块，A是这个模块下的一个类）
|   |
|   |--new_count.py（模组、类库、模块，B是这个模块下的一个类）
|
|--test.py（调用程序）
'''
#引用‘count’模块下的‘A’类的所有方法，“引用count模块下A类的所有方法”
from count import A

#告诉调用此模块的程序，(test.py)count是相对于new_count.py的一个引入
#修改后，执行"new_count"报错，所以还原修改，修改test.py文件
#from .count import A

#在‘new_count’这个模块下创建类‘B’，类‘B’继承类‘A’的所有方法（函数）
class B(A):

    def sub(self, a, b):
        return a - b

#所以类‘B’可以直接调用类‘A’的‘add()’方法(函数)(a + b)
resule = B().add(1, 8) #“类”调用方法的写法格式： B().add(a, b),一定是类() 点(.) 方法(函数)

print("‘new_count’的输出结果:", resule)

#print(B().add(2, 5))
#resules = B().sub(2, 5)
#print(B().sub(2, 5))
#print(resules)