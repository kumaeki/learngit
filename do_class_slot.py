class Student(object):
    __slots__ = ("name","age")




s = Student()
s.name = "kuma"
s.age=32
#s.score=30



class GraduateStudent(Student):
    pass


g= GraduateStudent()
g.score = 99
