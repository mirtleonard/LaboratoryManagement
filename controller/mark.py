from domain.student import Student_Validator
from domain.problem import Problem_Validator

class Mark:
    """
        Class that represents student-problem
    """

    __count = 0

    def __init__(self, student, problem, mark):
        self.__id = self.__count
        self.__student = student
        self.__problem = problem
        self.__mark = mark
        self.__count += 1

    def get_problem(self):
        return self.__problem

    def get_student(self):
        return self.__student

    def get_mark(self):
        return self.__mark

    def get_id(self):
        return self.__id

    def set_problem(self, new_problem):
        self.__problem = new_problem

    def set_student(self, new_student):
        self.__student = new_student

    def set_mark(self, new_mark):
        self.__mark = new_mark

    def __str__(self):
        answer = "| Student | Problem | Mark |\n____________________________\n"
        answer += str(self.__student) + ' | ' + str(self.__problem) + ' | ' + str(student_mark.__mark) + '\n'
        return asnwer

class Mark_Validator:
    """
        Class wich validates the assignment
    """
    def validate_mark(self, student_mark):
        if student_mark.get_mark() < 0 or student_mark.get_mark() > 10:
            raise ValidationError("Mark is invalid!")
