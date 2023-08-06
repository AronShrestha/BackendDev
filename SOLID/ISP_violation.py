from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

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

    def fly(self):
        
        raise Exception("Dog can't fly")
    

#here dog don't implement all the fuction in the interface so this oilets ISP




    
