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

    def delete_problem(self, id):
        """
            if id exists, will delete problem with id from repository
            id - int
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem with ID does't exit!")
        del self.__problems[id]

    def find_problem(self, id):
        """
            if problem with id exists, will be returned
            id- int
            return - Problem object
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem not found!")
        return self.__problems[id]

    def update_problem(self, id, description, deadline):
        """
            if problem exists, will be updated with values
            id - int
            description - string
            deadline - string
        """
        if not id in self.__problems:
            raise Repository_Exception("Problem with ID doesn't exits")
        problem = self.__problems[id]
        problem.set_description(description)
        problem.set_deadline(deadline)
        self.__problems[id] = problem

    def get_all(self):
        """
            returns all problems from repo
        """
        return self.__problems.values()

    def size(self):
        """
            return the number of problems in the repository
        """
        return len(self.__problems)

    def __str__(self):
        """
            returns all the students in repository
        """
        string =  "| ID | Description | Deadline |\n"  +  "_______________________________\n"
        for problem in self.__problems.values():
            string += str(problem.get_id()) + " " + problem.get_description() + " " + problem.get_deadline() + "\n"
        return string
