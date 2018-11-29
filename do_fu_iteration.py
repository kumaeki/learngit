# -*- coding: utf-8 -*-
def findMinAndMax(L):
    length = len(L)
    if length == 0:
        return (None,None)
    else:
        min = L[0]
        max = L[0]
        
        for i in L[1:]:
            if i < min:
                min = i
            if i> max:
                max = i
        return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')
