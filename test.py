from functools import partial
int2 = partial(int,base=2)
print(int2('1000'))

print(int2('1000' ,base=10))


max2 = partial(max,10)
print(max(1,3,6))
print(max2(1,3,6))
