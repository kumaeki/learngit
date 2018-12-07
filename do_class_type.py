# -*- coding: utf-8 -*-

class myObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj=myObject()
print(obj.power())

print(hasattr(obj,"x"))
print(hasattr(obj,"y"))

setattr(obj,"y",9)
print(hasattr(obj,"y"))

print(getattr(obj,"z",10))