import random
from domain.mark import *

class Mark_Controller:
    """
      Class responsible with the use cases related to Mark CRUD
      GRASP Controller
    """
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def add(self, student_id, problem_id, mark, student_repo, problem_repo):
        """
            if student_problems is valid, will add it to repository
            student - object of Student type
            problem - object of Problem type
        """
        student = student_repo.find(student_id)
        problem = problem_repo.find(problem_id)
        student_mark = Mark(student, problem, mark)
        self.__validator.validate(student_mark)
        self.__repository.add(student_mark)

    def find(self, id):
        """
            finds mark after id
        """
        try:
            return self.__repository.find(id)
        except:
            return -1

    def get_repository(self):
        """
            return student, repository
        """
        return self.__repository

    def delete(self, id):
        """
            deletes mark with id from repository
            id - int
        """
        self.__repository.delete(id);

    def search_by_problem(self, problem):
        """
            if exist marks with problem description, will be returned
            description - string
            return - list of Marks objects
        """
        marks = self.__repository.get_all()
        result = []
        for mark in marks.values():
            if type(problem) == type(0):
                if problem == mark.get_problem().get_id():
                    result.append(mark);
            elif problem in mark.get_problem().get_description():
                result.append(mark)
        return result

    def search_by_student(self, student):
        """
            if marks with student exists, will be returned
            name - string
            return - list of Marks objects
        """
        marks = self.__repository.get_all()
        result = []
        for mark in marks.values():
            if type(student) == type(0):
                if student == mark.get_student().get_id():
                    result.append(mark)
            elif student in mark.get_student().get_name():
                result.append(mark)
        return result

    def random(self, entities, students, problems):
        """
            adds x random marks
        """
        students = list(students.values())
        problems = list(problems.values())
        if len(students) == 0 or len(problems) == 0:
            raise Exception("There are no students or problems!")
        if len(students) * len(problems) - self.__repository.size() < entities:
            print("There are too little students and problems to create different marks!")
            entities = len(students) * len(problems) - self.__repository.size()
        while (entities):
            student = students[random.randint(0, len(students) - 1)]
            problem = problems[random.randint(0, len(problems) - 1)]
            mark = random.randint(1, 10)
            student_mark = Mark(student, problem, mark)
            try :
                self.__repository.add(student_mark)
                entities -= 1
            except :
                pass
