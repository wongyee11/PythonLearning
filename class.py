#!/usr/bin/env.python
# coding=utf-8

print("在面对对象编程的世界里，一切皆为对象，抽象的一组对象就是类")
print("例如，汽车是一个类，而我家的奔驰汽车就是一个具体的对象")
print("Python里用class关键字来创建类")
print("上面创建了一个A类（在Python3里‘object‘为所有类的基类，所有类在创建时默认继承‘object‘，所以不声明继承‘object‘也可以）")
print("在类下面创建了一个add()方法，方法的创建同样使用关键字‘def’，唯一不同的是，方法的第一个参数必须是存在的")
print("一般习惯命名为‘self’，但是在调用这个方法时不需要为这个参数传值")
class A(object):
    def add(self, a, b):
        return a + b
count = A()
print(count.add(1, 8))

print("一般在创建类时会首先声明初始化方法__init__()")
print("注意：init的两侧是‘双下划线__’,当我们在调用该类时，可以用来进行一些初始化工作")
class A():

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

count = A('1', 8) #给参数传值的时候必须用逗号‘，’分开两个参数的赋值
print(count.add())

print("Python里类的继承")
print("首先，我们创建一个‘A’类，在其下面创建add()方法计算两个参数相加")
print("接着创建‘B’类，继承‘A’类，并且又继续创建了sub()方法用于计算两个参数相减")
class A():

    def add(self, a, b):
        return a + b

class B(A):

    def sub(self, a, b):
        return a - b

print("因为‘B’类继承了‘A’类，所以‘B’类自然也拥有了add()方法，从而可以直接通过‘B’类调用add()方法")
print(B().add(1, 8))
#print(B().sub(5, 6))
#print(A().add(1, 8))