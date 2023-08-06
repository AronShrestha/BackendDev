# The Factory Design Pattern

The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created. It is used to create objects in a superclass, while delegating the responsibility of creating specific object instances to its subclasses.

## Problem:
Imagine you have a system where you need to create different types of objects, and the type of object to be created is determined at runtime based on certain conditions. You want to decouple the object creation from the rest of your code and make it more flexible and maintainable.

## Solution:
The Factory Design Pattern introduces a factory interface or base class that declares a method for creating objects. Subclasses of this factory implement this method to produce concrete instances of objects.

## Participants:

    Product: The abstract base class or interface that defines the common interface for the different types of objects the factory creates.
    ConcreteProduct: Concrete implementations of the Product interface.
    Creator: The abstract class or interface that declares the factory method for creating objects. It may also contain other methods that operate on the created objects.
    ConcreteCreator: Subclasses of the Creator class that implement the factory method to create instances of ConcreteProduct.

## Benefits:

    Flexibility: You can easily introduce new types of objects without modifying the existing codebase by creating new ConcreteProduct classes and corresponding ConcreteCreator classes.
    Encapsulation: Object creation logic is encapsulated within the factory classes, isolating it from the rest of the code.
    Code Organization: The pattern helps organize your code by separating object creation from other business logic.