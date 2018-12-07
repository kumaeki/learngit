import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def stu2dic(stu):
    return{
        "name":stu.name,
        "age":stu.age,
        "score":stu.score
    }

s = Student("kuma",33,99)
j = json.dumps(s,default=stu2dic)
print(j)

f = open("D:\\GIT_other\\learngit\\test\\test.txt","w")
f.write(j)
f.close()

