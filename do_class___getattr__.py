class Student(object):

    def __init__(self):
        self.name = "kuma"

    def __getattr__(self,attr):
        if attr=="score":
            return 99
        if attr=="age":
            return lambda x:x
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.name)
print(s.score)
print(s.age(33))
print(s.weight)
