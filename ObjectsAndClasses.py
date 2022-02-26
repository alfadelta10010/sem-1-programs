class Person:
    status = "Vaccinated"  # Class Variable

    def display(self):
        print("Height: {}, Age: {}".format(self.h, self.a))
        print("Status: {}".format(self.status))

    def __init__(self, height, age):  # Parametrized constructor
        self.h = height  # h is the instance variable
        self.a = age  # a is instance variable


jenny = Person(5.7, 25)
jenny.display()
print(jenny.status)
# or
Person.display(jenny)


# Encapsulation: Wrapping of data
# To restrict scope, we have two access specifiers, public and private
# Setter and getter methods are used to access private members outside the class


class Encapsulation:
    __a = 10  # Class variable

    def __display(self):
        print("python")

    def setName(self, n):  # To assign some value to class variable
        self.__a = n

    def getName(self):  # To retrieve the value of the variable
        return self.__a

    def call(self):
        self.__display()


obj1 = Encapsulation()
# print(obj1.__a)  # Not gonna work cause private
# obj1.__display()  # Not gonna work cause private
print(obj1.getName())
obj1.setName(69)
print(obj1.getName())
obj1.call()


# Inheritance - acquiring the properties
class Parent:
    def display(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("CHILD")


obj1 = Parent()
obj2 = Child()
obj2.display()


# Single inheritance, multilevel inheritance, multiple inheritance

class A:  # Grandparent class
    def functionA(self):
        print("Func A")


class B(A):  # Parent class
    def functionB(self):
        print("Func B")


class C(B):  # Parent class
    def functionC(self):
        print("Func c")


obj1 = C()
obj1.functionA()


# Polymorphism: One thing takes multiple forms
# 4 ways: Duck typing, operator overloading, method overloading, method overriding
# Duck typing: Related to dynamic typing (type of object is less important)
#   If a bird walks like a duck, swims like a duck and quackes like a duck, it's a uck.

class Duck:
    def sound(self):
        print("Quack")


class Dog:
    def sound(self):
        print("Woof")


class Cat:
    def sound(self):
        print("Meow")


def all_sound(obj):
    obj.sound()


x = Duck()
all_sound(x)


# 3. Method overloading: If there are 2 methods with the same name but diff arguments in the same class
# 4. Method overriding: If there are 2 methods with the same name and same number of arguments in two diff classes which implements inheritance

class student:
	def add(self, a, b):
		sum = a + b
		return sum
	def add(self, a, b, c):
		sum = a + b + c
		return sum
s1 = student()
print(s1.add(3, 2))
print(s1.add(3, 2, 5))


class A:
    def display(self):
        print("Func A")


class B(A):
    def display(self):
        print("Func B")
b1=B()
b1.display()