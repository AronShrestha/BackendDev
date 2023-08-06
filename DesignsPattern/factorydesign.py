from abc import ABC, abstractmethod


class Module:
    """
    for making more complex thing we may need to make this module an abstract class
    """
    pass
    # def __init__(self) -> None:
        
    #     self.module = []

    # def add_module(self, module):
    #     self.module.append(module)

    # def show_module(self):
    #     for i in range(len(self.module)):
    #         print(self.module[i])

    # def module_designer(self):
    #     e = Exercise_module()
    #     c = Concept_module()
    #     self.module.extend([e, c])

class Exercise_module(Module):
    def __init__(self) -> None:
        self.module_name = "Exercise"

    def __str__(self) -> str:
        return "Exercise Course"


class Concept_module(Module):
    def __init__(self) -> None:
        self.module_name = "Exercise"
    
    def __str__(self) -> str:
        return "Concept Course"


class Course:

    def __init__(self) -> None:
        self.Module = []
    
    def getModule(self):
        print(self.Module)

    @abstractmethod
    def create_course():
        pass


class HLD(Course):

    def create_course(self):
        self.Module.append(Exercise_module())
        self.Module.append(Concept_module())

    def __str__(self) -> str:
        return "HLD Course"


class LLD(Course):

    def create_course(self):
        self.Module.append(Exercise_module())
    
    def __str__(self) -> str:
        return "LLD Course"
     

class CourseFactory:
    
    def getCourses(self, course):
        courses = { 
            "HLD": HLD(),
            "LLD": LLD()}
        if course in courses:
            return courses[course]
        else:
            return None

        
def main():
    # m = Module()
    # m.module_designer()
    # m.show_module()

    course1 = CourseFactory().getCourses("HLD")  
    print(type(course1))
    course1.create_course()
    course1.getModule()
    course2 = CourseFactory().getCourses("LLD")
    course2.create_course()
    course2.getModule()
    

if __name__ == "__main__":
    main()
