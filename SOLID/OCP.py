from abc import ABC, abstractmethod

from OCP_violation import Person


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJson(PersonStorage):
    def save(self, person):
        print(f'Save the person {person} to a JSON file')


class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to an XML file')


if __name__=='__main__':
    person = Person('Aron Talcha')
    storage = PersonXML()
    storage.save(person)