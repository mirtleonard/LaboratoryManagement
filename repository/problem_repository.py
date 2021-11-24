from domain.problem import *
from repository.repository_exception import *

class Problem_Repository:
    """
        Class responsible for managing a list of problems  (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__problems = {}

    def add_problem(self, id, description, deadline):
        """
            If problem is valid, will add it to repository
            id - int
            description - string
            deadline -string
        """
        problem = Problem(id, description, deadline)
        problem_validator = Problem_Validator()
        problem_validator.validate_problem(problem)
        if id in self.__problems:
            raise Repository_Exception("Problem ID already exists.")
        self.__problems[id] = problem

    def getAll(self):
        """
            returns all problems from repo
        """
        return self.__problems.values()

    def size(self):
        """
            return the number of problems in the repository
        """
        return len(self.__problems)
