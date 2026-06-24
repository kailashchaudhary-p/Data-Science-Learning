class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()

obj.sound()
obj.bark()


class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()

obj.skill1()
obj.skill2()


class GrandFather:
    def house(self):
        print("Grandfather's House")

class Father(GrandFather):
    def car(self):
        print("Father's Car")

class Son(Father):
    def bike(self):
        print("Son's Bike")

obj = Son()

obj.house()
obj.car()
obj.bike()


class Animal:
    def eat(self):
        print("Animals Eat")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

class Cat(Animal):
    def meow(self):
        print("Cat Meows")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()


class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()

obj.show()

class Student:
    def __init__(self):
        self.name = "John"

obj = Student()

print(obj.name)


class Student:
    def __init__(self):
        self._name = "John"

class Child(Student):
    def display(self):
        print(self._name)

obj = Child()
obj.display()


class Student:
    def __init__(self):
        self.__marks = 95

    def display(self):
        print(self.__marks)

obj = Student()

obj.display()


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

obj = Dog()

obj.sound()


class Calculator:

    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = Calculator()

obj.add(10)
obj.add(10,20)
obj.add(10,20,30)


class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

obj = Dog()

obj.sound()


print(10 + 20)

print("Hello " + "Python")

print([1,2] + [3,4])