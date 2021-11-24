from domain.student import *

class Student_Repository:
    """
        Class responsible for managing a list of students (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__students = {}

    def add_student(self, id, name, group):
        """
            if student is valid, will add it in respository
        """
        student = Student(id, name, group)
        student_validator = Student_Validator()
        student_validator.validate_student(student)
        if id in self.__students:
            raise Repository_Exception("Student ID already exists.")
        self.__students[id] = student

    def delete_student(self, id):
        pass

    def getAll(self):
        pass

    def size(self):
        """
            return the number of students in the repository
        """
        return len(self.__students)

class Repository_Exception(Exception):
    """
      Base class for the exceptions in the repository
    """
    def __init__(self, msg):
        self.__msg = msg
    def get_msg(self):
        return self.__msg
    def __str__(self):
        return self.__msg