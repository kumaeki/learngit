# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def print_inf(self):
        print("%s : %s" %(self.name,self.age))



kuma = Student("kuma","32")
kuma.print_inf()
