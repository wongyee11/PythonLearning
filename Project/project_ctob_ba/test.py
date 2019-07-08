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
#引用“sys”类（模块）
import sys
#将“model”所在目录添加到“path”的搜素目录
sys.path.append("./model")
#引用‘model’模组（类库、模块）下的‘new_count’这个模块里类的方法
from model import new_count

#调用
test = new_count.B()
test.add(4, 5)

print("'test'的输出结果:", test.add(4, 5))
#print("'test'的输出结果:", test.sub(4, 5))
#print(sys.path)