import random
import datetime
from domain.problem import *

class Problem_Controller:
    """
      Class responsible with the use cases related to Problem CRUD
      GRASP Controller
    """
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def add(self, id, description, deadline):
        """
            if problem is valid, will add it in respository
            id - int
            description - string
            deadline - int
        """
        problem = Problem(id, description, deadline)
        self.__validator.validate(problem)
        self.__repository.add(problem)

    def find(self, id):
        """
            finds problem after id
        """
        return self.__repository.find(id)

    def get_repository(self):
        """
            return student, repository
        """
        return self.__repository

    def delete(self, id):
        """
            deletes problem with id from repository
            id - int
        """
        self.__repository.delete(id);

    def search(self, description):
        """
            if exist problems with description, will be returned
            description - string
            return - list of Problems objects
        """
        problems = self.__repository.get_all()
        result = []
        for problem in problems.values():
            if description in problem.get_description():
                result.append(problem);
        return result

    def update(self, id, description, deadline):
        """
            if problem exists, will be updated with values
            id - int
            description - string
            deadline - string
        """
        new_problem = Problem(id, description, deadline)
        self.__validator.validate(new_problem)
        old_problem = self.__repository.find(id)
        self.__repository.update(id, new_problem)

    def random(self, entities):
        """
            adds x random problems
        """
        while (entities):
            id = random.randint(0,1000)
            description = ""
            for i in range(20):
                description += chr(ord('a') + random.randint(0, 26))
            deadline = datetime.date(2021,1,1) + datetime.timedelta(days = random.randint(0,100000))
            deadline = str(deadline)
            problem = Problem(id, description, deadline)
            try:
                self.add(id, description, deadline)
                entities -= 1
            except:
                continue
