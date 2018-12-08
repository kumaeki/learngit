# -*- coding: utf-8 -*-
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("before call : %s" % func.__name__)
        r = func(*args,**kw)
        print("after call : %s" % func.__name__)
        return r
    return wrapper

def log2(arg):
    if isinstance(arg,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("before call : %s" % func.__name__)
                print("text : %s" % arg)
                r = func(*args,**kw)
                print("after call : %s" % func.__name__)
                return r
            return wrapper
        return decorator

    else:
        @functools.wraps(arg)
        def wrapper(*args,**kw):
            print("before call : %s" % arg.__name__)
            r = arg(*args,**kw)
            print("after call : %s" % arg.__name__)
            return r
        return wrapper



@log2
def now():
    print("2018-12-01")

@log2("has param")
def now2():
    print("2018-12-01 second")

now()
now2()

