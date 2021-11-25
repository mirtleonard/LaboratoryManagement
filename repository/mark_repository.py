from controller.mark import *
from repository.repository_exception import *

class Mark_Repository:
    """
        Class responsible for managing a list of student_problem (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__marks = {}

    def assign(self, student_id, problem_id, mark, student_repo, problem_repo):
        """
            if student_problems is valid, will add it to repository
            student - object of Student type
            problem - object of Problem type
        """
        try:
            student = student_repo.find_student(student_id)
            problem = problem_repo.find_problem(problem_id)
        except Exception as error:
            raise Repository_Exception(error)
        student_mark = Mark(student, problem, mark)
        mark_validator = Mark_Validator()
        mark_validator.validate_mark(student_mark)
        self.__marks[student_mark.get_id()] = student_mark

    def __str__(self):
        """
            Retrun the marks as strings
        """
        answer = "| Student | Problem | Mark |\n____________________________\n"
        for student_mark in self.__marks.values():
            answer += student_mark.get_student().get_name() + ' | ' + student_mark.get_problem().get_description() + ' | ' + str(student_mark.get_mark()) + "\n"
        return answer
