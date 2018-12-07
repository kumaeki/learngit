# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):

        if not isinstance(name,str):
            raise ValueError("wrong param : name")
        if gender != "male" or gender != "female":
            raise ValueError("wrong param : gender")
        
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        self.__name = name

    def set_gender(self,gender):
        self.__gender=gender



# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('1测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('2测试失败!')
    else:
        print('3测试成功!')

bart = Student('Bart', '1')
