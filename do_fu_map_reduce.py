# -*- coding: utf-8 -*-
from functools import reduce

DICTS= {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}

def str2float(s):
    def char2num(c):
        return DICTS[c]

    flg = True
    point = 1
    def fn(x,y):
        nonlocal flg
        nonlocal point
        if y == '.':
            flg = False
            return x
            
        if flg:
            return x*10 + y
        else:
            point=point*0.1
            return x+y*point


    return reduce(fn,map(char2num,s))





print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
