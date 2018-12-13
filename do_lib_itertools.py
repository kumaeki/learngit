import itertools

natruals = itertools.count(-1)
ns = itertools.takewhile(lambda x:x<100,natruals)
print(list(ns))


cycles = itertools.cycle("abc")
n = 1
for c in cycles:
    print(c)
    n += 1
    if n == 10:
        break

rs = itertools.repeat("zpc",4)
for r in rs:
    print(r)


for c in itertools.chain("12","45"):
    print(c)


for key,group in itertools.groupby("AaaBBbbbccCCc",lambda c:c.upper()):
    print(key,list(group))