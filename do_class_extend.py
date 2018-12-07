# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    def run(self):
        print("dog is running")

class Cat(Animal):
    def run(self):
        print("cat is running")

class Car(object):
    def run(self):
        print("car is running")    


def run_twice(a):
    a.run()
    a.run()



run_twice(Dog())

run_twice(Cat())

run_twice(Car())
    
