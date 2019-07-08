#!/usr/bin/env.python
# coding=utf-8

print("Python规定一个字典中的key必须独一无二，value可以相同")
print("字典用花括号'{}'表示，里面的项成对出现，一个key对应一个value；key与value之间用冒号':'分隔，不同的项之间用逗号','分隔")
dicts = {"username":"zhangsan",'password':12345}

print("keys()函数返回字典key的列表")
dicts.keys()
print(dicts.keys())

print("values()函数返回字典value的列表")
dicts.values()
print(dicts.values())

print("items()函数将所有的字典项以列表方式返回")
dicts.items()
print(dicts.items())
print("这些列表中的每一项都包含key和value，但是项在返回时并不会按照它们在字典中的存放顺序")
for k,v in dicts.items():
    print("dicts key is %r " %k)
    print("dicts values is %r " %v)
    print(k, v)

print("通过zip方法合并两个List为Dictionary，遍历会按存放的顺序")
keys = ["b","a","c","e","d"]
values = ["2","1","3","5","4"]

for key,value in zip(keys,values):
    print(key,value)