# SOLID Principles

The SOLID principles are a set of five design principles for writing maintainable, scalable, and flexible software. These principles were introduced by Robert C. Martin and are widely used in object-oriented programming. Each principle focuses on a specific aspect of software design and aims to make the code more robust and easier to maintain.
<br><br><br>

## 1) Single Responsibility Principle:
Any module [module=="Set of functions or functionality, class of Package,or Source code "] ->only 1 actor can change this i.e
<br><br>
Consider a class called Employee and it has three different method 1) CalculateSaary ,
        2) CalculateHours,
        3) saveEmpData
    Calculate salary is used by CFO of that office 
    CalculateHours is used by the HR 
    Savingemployedata is required by the Technical employee 
    So there are three different Actors/Shareholders

    Consider the sample defination of the function 

    [public func] int calculateSalary(**datat){
....
....
getRegularHours(...);
....
....
    }


        [public func] int calculateSalary(**datat){
....
....
getRegularHours(...);
....
....
    }



[private func] int getRegularHours(...){

}


[public func] int calculateHours(....){
    ....
    ....
    getRegular Hours(..);
    ....
    ...
}

Here, if there is any kind of change calculateSalary method by the CFO , then this calculation function will change in this class and it might require you to change in the getRegularHours(...) private func as well, now to method has been changed .
Now calculateHours to be used by HR is also using the getRegularHours() private method internally there this the chance that this implementation breaks because of the change in the getRegulaarHours method.
<br><br>
All in all, the CFO required a changed to be made internally and  HR is getting some wrong data beacuse someone(here CFO) changed the underlie implementation of the private method which was used by both these public method.
<br>
Here, One class  exposed two or three different public methods which were corresponding to different stakeholders or the actors. One actor doesn't know about the other actor but still the change requested from one actor impaced the other one so this here is the breaking of the single responsobility principle.Because this module is encapsulationg the different function or functionalities which cater to different actors of the system and this what single responsibility principles means that the code your writing , if that code request changes from ony one actor or one stakehoder or even group of one stakeholder which fulfill one business requirement till that point is fine, however if one class has changes being requested  from different stakeholders that menans you have treid to put towards three different business functionalities together in one module and this is the point where we have broken the singlw responsibility principle.
 
 A way to solve it is to break into different classes :
 make CalculateSalaryClass, CalculateHoursClass, storedataclass.And all thos classes can be called from the different parts of the program and the calculation of salary doen't need to know about or depen on any method that is used in calculate hours similary saving the employeed data to some database doen't need to know about calaculate salary or calculate hours at all.
 This way while by seperating the class or by decomposing one class into multiple classes  we can actually adhere to SRP, where the business function or req or business logic sits in the particular classes and the request for changing those business logic can only come from one particular stakeholder.


 <br><br><br>
 In short , a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes.

 ### note :if you follow this principle blindly and break down your code into atomic sections, this also leads to some undesired side effects. There should be a balancing consideration, and the below quote defines what it is;

 ### Gather together the things that change for the same reasons. Separate those things that change for different reasons — Robert C.Martin



 <br><br><br><br>

 ## ) Open/Closed Principle:

 ###### Open for Extension and 
 ###### Closed for modification
 <br><br>
We should be able to add new features to the class without affecting the old code. This is because whenever we edit old code, we run the risk of introducing potential problems. So, if at all possible, we should avoid touching the proven and trudtworthy(mainly) prduction code.

Example: 
a tourist comapny provides the package which includes:
1)Flights
2) Hotel
3) Guided tour 
now lets say there are few customers that are requesting for some more addition to the package, they want complimntary breakfast but that is not comming into h budget of this package. So what they do is they add the complementary  breakfast but they modify the flights so they would say okay we'll give you one way of the flights ticket but we will not give you the returning tikets which might not work with the  existing customer.So the toursit company edited their package for some new customer but that change of package might not work for the old customer and might not work for some new customer as well and this is also breaking our open close principle bcause their basic functionality they have opened it for modification which is not accepted in our solid principle.
So what can we do to make it comply  our open close principle  
so the toursit company should not touch their baisc package which includes flight, hotel and guided tour and tif they want to add complementary breakfast they should throw in the complementary breakfast for their new customers but  they should not be touching the old package and that would follow our open close principle. 
So, as per OCP your basic functionality should be close dfor modification.



## 3) Liskov Substitution Principle:
Let f(x) be a property provable about objects x of type T. Then f(y) should be true for objects y of type S where S is a subtype of T. i.e  "Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program"("In other words, subclasses should be able to substitute their base classes without altering the desired behavior of the program.")

![Alt Text][image_reference]

[image_reference]: images/1.png "LSP"

![Alt Text][image_reference]

[image_reference]: images/2.png "LSP"


If a function takes an  instance of a class. That same function should also be able to take the instance of derived class from that class 

How to know LSP is violated or not:
1)  First check if inheritance of the class is done in the preoper manner or not (ASK yourself is the child class is really is a type of parent class)
2)  Always try to replace the instances of parent class with the child class and see if it breaks any underlying functionality.

<br><br><br>

## 4) Interface Segregation Principle(ISP):
#### Interfaces [{ keep things abstract(hiding details) and let classes implement them }]
 
#### But
Prolems are : Fat interfaces , Include a lot of functionality, Hide a lot of functionality

#### SO 
Design interfaces in such a way that the classes that implement those interfaces does not have many unused functions. 


###### The interface segregation principle states that an interface should be as small a possible in terms of cohesion. In other words, it should do ONE thing.It doesn’t mean that the interface should have one method. An interface can have multiple cohesive methods.

<br><br><br>

## 5)Dependency Inversion Principle (DIP):
Principle of dependancy inversion != Application of Dependency Inversion

High level module should not depend on low level modules. Both should depend on abstractions. Abstraction should not depends on implemention. Implementation should depends on abstraction.

Simplifying,
High level modules or low level modles in your code should not depends on the acutal implementation, they should depend on abstractions(->Interfaces)

![Alt Text][image_reference]

[image_reference]: images/3.png "DIP"


#### The dependency inversion principle states that:

 ####   High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

#### The dependency inversion principle aims to reduce the coupling between classes by creating an abstraction layer between them.