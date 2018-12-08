# -*- coding: utf-8 -*-
def is_palindrome_2(n):
    _stri_n = str(n)
    length = len(_stri_n)
    index = 0
    _stri_n_palidrome =  ""
    while index < length:
        _stri_n_palidrome += _stri_n[length-1-index]
        index += 1

    return int(_stri_n_palidrome) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]
    

    






# 测试:
output = filter(is_palindrome, range(1, 200))
print('1~200:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
