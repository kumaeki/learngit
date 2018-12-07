class Chain(object):

    def __init__(self,path=""):
        self.path = path


    def __getattr__(self,path):
        return Chain("%s/%s" % (self.path,path))

    def __str__(self):
        return self.path

    __repr__ = __str__

    def __call__(self,path):
        return Chain("%s/:%s" % (self.path,path))


print(Chain().status.user.timeline.list)
print(Chain().status.user("kuma").timeline.list)
