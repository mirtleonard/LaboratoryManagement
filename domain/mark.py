from domain.student import Student_Validator
from domain.problem import Problem_Validator

class Mark:
    """
        Class that represents student-problem
    """

    def __init__(self, student, problem, mark):
        self.__id = str(student.get_id()) + "-" + str(problem.get_id())
        self.__student = student
        self.__problem = problem
        self.__mark = mark

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

    def __eq__(self, other):
        if isinstance(other, Mark):
            return other.get_id() == self.__id and other.get_problem() == self.__problem and other.get_mark() == self.__mark and other.get_student() == self.__student
        return False

    def __str__(self):
        return str(self.__student.get_id()) + ' | ' + str(self.__problem.get_id()) + ' | ' + str(self.__mark)

class Mark_Validator:
    """
        Class wich validates the assignment
    """
    def validate(self, student_mark):
        if student_mark.get_mark() <= 0 or student_mark.get_mark() > 10:
            raise ValidationError("Mark is invalid!")
