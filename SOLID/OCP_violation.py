class Person:
    def __init__(self, name):
        self.name = name 
    
    def __repr__(self):
        return f'Person(name={self.name})'
    

class PersonStorage:
    def save_to_database(self, person):
        print(f'Save the {person} to database')
    
    def save_to_json(self, person):
        print(f'Save the {person} to a JSON file')



if __name__ == '__main__':
    person = Person("Aron Ashesh")
    storgae = PersonStorage()
    storgae.save_to_database(person)


# In this example, there is a class called PersonStorage with two methods: save_to_database() 
# and save_to_json(). These methods are used to save a person's information to either a database or a JSON file.

# However, the problem arises when you want to add the functionality of saving a 
# person's information to an XML file. To do this, you need to modify the PersonStorage
# class, adding a new method for saving to XML. This violates the open-closed principle
#  because the class is not open for extension without modification.

# In simpler terms, the open-closed principle means that you should be able to add new 
# features to a class without changing its existing code. But in this example, adding the 
# ability to save to XML requires changing the PersonStorage class, which is not ideal according to
#  the open-closed principle.
