import random
from domain.problem import *
from repository.repository_exception import *

class Problem_Repository:
    """
        Class responsible for managing a list of problems  (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__problems = {}

    def add(self, problem):
        """
            If problem is valid, will add it to repository
            id - int
            description - string
            deadline -string
        """
        if problem.get_id() in self.__problems:
            raise Repository_Exception("Problem ID already exists.")
        self.__problems[problem.get_id()] = problem

    def delete(self, id):
        """
            if id exists, will delete problem with id from repository
            id - int
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem with ID does't exit!")
        del self.__problems[id]

    def find(self, id):
        """
            if problem with id exists, will be returned
            id- int
            return - Problem object
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem not found!")
        return self.__problems[id]

    def update(self, id, new_problem):
        """
            if problem exists, will be updated with values
            id - int
            description - string
            deadline - string
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem with ID doesn't exits")
        self.__problems[id] = new_problem

    def get_all(self):
        """
            returns all problems from repo
        """
        return self.__problems

    def size(self):
        """
            return the number of problems in the repository
        """
        return len(self.__problems)
