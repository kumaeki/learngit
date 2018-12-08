# -*- coding: utf-8 -*-
import time, functools

def log(func):
    def warpper(*args,**kw):
        print("call %s :" % func.__name__)
        return func(*args,**kw)
    return warpper

@log
def now():
    print("2018-12-01")

now()


