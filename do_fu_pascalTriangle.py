# -*- coding: utf-8 -*-

def triangles():
    n=0
    L1=[]
    L2=[]
    while True:
        if n==0:
            L2=[1]
        elif n==1:
            L2=[1,1]
        else:
            L2=[]
            for l in range(n+1):
                
                if l==0:
                    L2.append(1)
                elif l==n:
                    L2.append(1)
                else:
                    L2.append(L1[l-1]+L1[l])
        n+=1
        L1=L2
        yield L2


def triangles_2():
    L=[1]
    while True:
        yield L
        L=[sum(i) for i in zip([0]+L,L+[0])]
        


t=triangles_2()
for index in range(10):
    print(next(t))
