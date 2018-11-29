# -*- coding: utf-8 -*-

def product(*numbers):

    result=1

    for number in numbers:
        result = result * number
    
    return result


def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

def fact_iter(n):
    return fact_iter_in(n,1)

def fact_iter_in(num,product):
    if num==1:
        return product
    else:
        return fact_iter_in(num-1,num*product)
    
