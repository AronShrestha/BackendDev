from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

class Bird(Animal):
    @abstractmethod
    def fly(self):
        pass


class Eagle(Animal):
    def walk(self):
        print("Walking")

    def fly(self):
        print("Flying high")


class Dog(Animal):
    def walk(self):
        print("Running")







    
