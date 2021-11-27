from domain.student import *
from repository.repository_exception import *

class Student_Repository:
    """
        Class responsible for managing a list of students (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__students = {}

    def add(self, student):
        """
            if student is valid, will add it in respository
            student - object of type Student
        """
        if student.get_id() in self.__students:
            raise Repository_Exception("Student ID already exists.")
        self.__students[student.get_id()] = student

    def delete(self, id):
        """
            if id exists, will delete student with id from repository
            id - int
        """
        if not id in self.__students:
            raise Repository_Exception("Student with ID does't exit!")
        del self.__students[id]

    def find(self, id):
        """
            if student with id exists, will be returned
            id - integer
        """
        if not id in self.__students:
            raise Repository_Exception("Student not found!")
        return self.__students[id]

    def update(self, id, new_student):
        """
            update student with values
            id - int
            student - object of type Student
        """
        student = self.__students[id]
        self.__students[id] = new_student

    def get_all(self):
        """
            returns all students from repo
        """
        return self.__students

    def size(self):
        """
            return the number of students in the repository
        """
        return len(self.__students)
