# -*- coding: utf-8 -*-

#class Hello(object):
#    def hello(self,name = "world"):
#        print("hello ,%s" % name)

#h = Hello()
#h.hello()
#print(type(Hello))
#print(type(h))


def fn(self,name="world"):
    print("hello , %s" % name)

Hello = type('Hello',(object,),dict(hello=fn))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))
