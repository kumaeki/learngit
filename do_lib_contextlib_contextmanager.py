from contextlib  import contextmanager

class Query(object):
    def __init__(self,name):
        self.name = name

    def query1(self):
        print("Query info about %s from query1... " % self.name)

    def query2(self):
        print("Query info about %s from query2... " % self.name)

    def query3(self):
        print("Query info about %s from query3... " % self.name)

@contextmanager
def create_query(name):
    print("Begin...")
    q = Query(name)
    yield q
    print("End...")

with create_query("kuma") as k:
    k.query1()
    k.query2()
    k.query3()
