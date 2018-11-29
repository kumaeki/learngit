# -*- coding: utf-8 -*-
def fib(max):
    n,a,b = 0,0,1
    while(n<max):
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'


def fib_gen(max):
    n,a,b = 0,0,1
    while(n<max):
        yield(b)
        a,b=b,a+b
        n+=1
    return 'done'

#print(fib(6))
#print(fib_gen(6))

#for f in fib_gen(6):
#    print(f)

g=fib_gen(6)
while True:
    try:
        x = next(g)
        print('g = ',x)

    except StopIteration as e:
        print('Generator return value:',e.value)
        break
        
