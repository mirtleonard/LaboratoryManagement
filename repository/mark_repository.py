import random
from domain.mark import *
from repository.repository_exception import *

class Mark_Repository:
    """
        Class responsible for managing a list of student_problem (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__marks = {}

    def add(self, student_mark):
        """
            if student_problems is valid, will add it to repository
            student - object of Student type
            problem - object of Problem type
        """
        if student_mark.get_id() in self.__marks:
            raise Repository_Exception("Mark ID already exists.")
        self.__marks[student_mark.get_id()] = student_mark

    def delete(self, id):
        """
            if id exists, will delete problem with id from repository
            id - int
        """
        if not id in self.__marks:
            raise Repository_Exception("Mark with ID does't exit!")
        del self.__marks[id]

    def find(self, id):
        """
            if mark with id exists, will be returned
            id - int
            return - Mark object
        """
        if not id in self.__marks:
            raise Repository_Exception("Mark not found!")
        return self.__marks[id]

    def get_all(self):
        """
            returns all marks from repo
        """
        return self.__marks

    def size(self):
        """
            return the number of marks in the repository
        """
        return len(self.__marks)
