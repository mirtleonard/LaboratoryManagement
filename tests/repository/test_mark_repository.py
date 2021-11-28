import unittest
from domain.mark import *
from domain.problem import *
from domain.student import *
from repository.mark_repository import *
from repository.student_repository import *
from repository.problem_repository import *


class Test_Mark_File_Repository(unittest.TestCase):
    def __setUp(self, file):
        self.__file = file
        self.__problem = Problem(1, "CMMDC", "24.11.2021")
        self.__student = Student(1, "Alin", 201)
        self.__student_repository = Student_Repository()
        self.__student_repository.add(self.__student)
        self.__problem_repository = Problem_Repository()
        self.__problem_repository.add(self.__problem)
        self.__repository = Mark_File_Repository(self.__file, self.__student_repository, self.__problem_repository)
        self.__mark = Mark(self.__student, self.__problem, 9)
        self.__repository.delete_all(file)

    def __test_add(self):
        self.__repository.add(self.__mark)
        assert self.__repository.find("1-1") == self.__mark
        test_repository = Mark_File_Repository(self.__file, self.__student_repository, self.__problem_repository)
        assert test_repository.find("1-1") == self.__mark
        self.__repository.delete_all(self.__file)

    def __test_remove(self):
        self.__repository.add(self.__mark)
        self.__repository.delete(self.__mark.get_id())
        assert self.__repository.size() == 0
        test_repository = Mark_File_Repository(self.__file, self.__student_repository, self.__problem_repository)
        assert test_repository.size() == 0
        self.__repository.delete_all(self.__file)

    def __test_update(self):
        self.__repository.add(self.__mark)
        new_mark = Mark(self.__student, self.__problem, 1)
        self.__repository.update('1-1', new_mark)
        assert self.__repository.find('1-1') == new_mark
        test_repository = Mark_File_Repository(self.__file, self.__student_repository, self.__problem_repository)
        assert test_repository.find('1-1') == new_mark
        self.__repository.delete_all(self.__file)

    def run_tests(self):
        self.__setUp("tests/test_mark.txt")
        self.__test_add()
        self.__test_update()
        self.__test_remove()
