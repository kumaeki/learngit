# -*- coding: utf-8 -*-
def trim(s):
    length = len(s)
    if length>0:
        for i in range(length):
            if s[i] != ' ':
                break

        j=length -1
        
        while s[j] == ' ' and j>=i:
            j=j-1
        s = s[i:j+1]
        print('i = ', i , ',j=',j+1)
    return s



if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')
        
