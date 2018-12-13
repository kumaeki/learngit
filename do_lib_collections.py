from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple("Point",["x","y"])
p = Point(1,2)
print("(%s,%s)" % (p.x,p.y))


q = deque(["a","b","c"])
print(q)

dd = defaultdict(lambda:"N/A")
dd["key1"]="abc"
print("dd['key1'] = %s" %dd["key1"])
print("dd['key2'] = %s" %dd["key2"])

#3.6开始dict开始排序
d = dict([("a",1),("b",2),("c",3),("d",4),("e",5),("f",6),("g",7)])
od = OrderedDict([("a",1),("b",2),("c",3),("d",4),("e",5),("f",6),("g",7)])
print(d)
print(od)

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity=capacity
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print("remove : ",last)
        if containsKey:
            del self[key]
            print("set : ",(key,value))
        else:
            print("add : ",(key,value))
        OrderedDict.__setitem__(self,key,value)

ld = LastUpdatedOrderedDict(3)
ld["a"]=1
ld["b"]=2
ld["c"]=3
print(ld)
ld["d"]=4
print(ld)
ld["b"]=2
print(ld)


c = Counter()
for ch in "programming":
    c[ch] = c[ch]+1
print(c)