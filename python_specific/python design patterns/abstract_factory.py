from __future__ import annotations
from abc import ABC, abstractmethod


# Abstract Product: Department
class DepartmentAbstractFactory(ABC):
    @abstractmethod
    def get_department_name(self):
        pass


# Concrete Products
class ComputerScienceConcreteFactory(DepartmentAbstractFactory):
    def get_department_name(self):
        return "Computer Sience Department"


class MathematicsConcreteFactory(DepartmentAbstractFactory):
    def get_department_name(self):
        return "Mathematics Department"
    

# Abstract factory interface for Public University
class PublicUniversityDepartmentAbstractFactory(ABC):
    def create_department(self):
        pass


# Concrete factory for Public University
class PublicComputerScienceFactory(PublicUniversityDepartmentAbstractFactory):
    def create_department(self):
        return ComputerScienceConcreteFactory()
    

# Abstract factory interface for PrivateUniversity
class PrivateUniversityDepartmentAbstractFactory(ABC):
    def create_department(self):
        pass


# Concrete factory for Public University
class PrivateMathematicsFactory(PrivateUniversityDepartmentAbstractFactory):
    def create_department(self):
        return MathematicsConcreteFactory()
    


# Clinet code 
def select_department(factory):
    department = factory.create_department()
    print("Selected Department:", department.get_department_name())


def main():
    pubic_department_factory = PublicComputerScienceFactory()
    private_departmnt_factory = PrivateMathematicsFactory()

    select_department(pubic_department_factory)
    select_department(private_departmnt_factory)

if __name__ == '__main__':
    main()
    




