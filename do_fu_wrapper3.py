# -*- coding: utf-8 -*-
import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, time.time()))
        return fn(*args,**kw)
    return wrapper


@metric
def doSomething():
    print(" do something")


doSomething()
