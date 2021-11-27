import random
from domain.student import *

class Student_Controller:
    """
      Class responsible with the use cases related to Student CRUD
      GRASP Controller
    """
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def add(self, id, name, group):
        """
            if student is valid, will add it in respository
            id - int
            name - string
            group - int
        """
        student = Student(id, name, group)
        self.__validator.validate(student)
        self.__repository.add(student)

    def find(self, id):
        """
            finds student after id
        """
        return self.__repository.find(id)

    def get_repository(self):
        """
            return student, repository
        """
        return self.__repository

    def delete(self, id):
        """
            if id exists, will delete student with id from repository
            id - int
        """
        self.__repository.delete(id);

    def search(self, name):
        """
            if exist students with name, will be returned
            name - string
            return - list of Student objects
        """
        students = self.__repository.get_all()
        result = []
        for student in students.values():
            if name in student.get_name():
                result.append(student);
        return result

    def update(self, id, name, group):
        """
            if student exists, will be updated with values
            id - int
            name - string
            group - int
        """
        new_student = Student(id, name, group)
        self.__validator.validate(new_student)
        old_student = self.__repository.find(id)
        self.__repository.update(id, new_student)

    def random(self, entities):
        """
            adds x number of students random
            entities - integer
        """
        while (entities):
            id = random.randint(0,1000)
            name = ""
            for i in range(6):
                name += chr(ord('a') + random.randint(0, 26))
            group = random.randint(0,1000)
            try:
                self.add(id, name, group)
                entities -= 1
            except:
                continue
