#!/usr/bin/env.python
# coding=utf-8

print("数组用方括号'[]'表示，里面的每一项用逗号','隔开")

print("Python允许在数组里面任意地放置数字或字符串")
lists = [1,2,3,'a',5]
lists
print(lists)

print("需要注意的是，数组下标是从0开始的，所以lists[0]会输出数组的第一项")
lists[0]
print(lists[0])

lists[4]
print(lists[4])

lists[4] = 'b'
lists[4]
print(lists[4])

print("append()函数可以向数组末尾追加新的项")
lists.append('c')
lists
print(lists)