from domain.student import Student_Validator
from domain.problem import Problem_Validator

class Mark:
    """
        Class that represents student-problem
    """
    id = 0

    def __init__(self, student, problem, mark):
        self.__id = Mark.id
        self.__student = student
        self.__problem = problem
        self.__mark = mark
        Mark.id += 1


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
        answer = str(self.__student.get_name()) + ' | ' + str(self.__problem.get_description()) + ' | ' + str(self.__mark) 
        return answer

class Mark_Validator:
    """
        Class wich validates the assignment
    """
    def validate(self, student_mark):
        if student_mark.get_mark() <= 0 or student_mark.get_mark() > 10:
            raise ValidationError("Mark is invalid!")
