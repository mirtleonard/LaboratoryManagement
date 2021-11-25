import random
from domain.student import *
from repository.repository_exception import *

class Student_Repository:
    """
        Class responsible for managing a list of students (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__students = {}

    def random(self, entities):
        """
            adds x number of students random
        """
        while (entities):
            id = random.randint(0,1000)
            name = ""
            for i in range(6):
                name += chr(ord('a') + random.randint(0, 26))
            group = random.randint(0,1000)
            student = Student(id, name, group)
            try:
                student_validator = Student_Validator()
                student_validator.validate_student(student)
            except:
                continue
            if id in self.__students:
                continue;
            entities -= 1
            self.__students[id] = student

    def add_student(self, id, name, group):
        """
            if student is valid, will add it in respository
            id - int
            name - string
            group - int
        """
        student = Student(id, name, group)
        student_validator = Student_Validator()
        student_validator.validate_student(student)
        if id in self.__students:
            raise Repository_Exception("Student ID already exists.")
        self.__students[id] = student

    def delete_student(self, id):
        """
            if id exists, will delete student with id from repository
            id - int
        """
        if not id in self.__students:
            raise Repository_Exception("Student with ID does't exit!")
        del self.__students[id]

    def find_student(self, id):
        """
            if student with id exists, will be returned
            id - int
            return - Student object
        """
        if not id in self.__students:
            raise Repository_Exception("Student not found!")
        return self.__students[id]

    def update_student(self, id, name, group):
        """
            if student exists, will be updated with values
            id - int
            name - string
            group - int
        """
        if not id in self.__students:
            raise Repository_Exception("Student with ID doesn't exits")
        student = self.__students[id]
        student.set_name(name)
        student.set_group(group)
        self.__students[id] = student

    def get_all(self):
        """
            returns all students from repo
        """
        return self.__students.values()

    def size(self):
        """
            return the number of students in the repository
        """
        return len(self.__students)

    def __str__(self):
        """
            returns all the students in repository
        """
        string =  "| ID | Name | Group |\n"  +  "_____________________\n"
        for student in self.__students.values():
            string += str(student.get_id()) + " | " + student.get_name() + " | " + str(student.get_group()) + "\n"
        return string
