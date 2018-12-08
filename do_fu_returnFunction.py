# -*- coding: utf-8 -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax +n
        return ax

    return sum

f1=lazy_sum(1,2,3,4,5)
f2=lazy_sum(1,2,3,4,5)
print(f1)
print(f2)


#def count():
#    fs=[]
#    for i in range(1,4):
#        def f():
#            return i * i
#        fs.append(f)
#    return fs

def count():
    def f(j):
        def g():
            return j*j
        return g

    fs = []

    for i in range(1,4):
        fs.append(f(i))
    return fs


f1,f2,f3=count()
print(f1())
print(f2())
print(f3())




def createCounter():
    L = [0]
    def counter():
        L[0] = L[0] + 1
        return L[0]
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')




