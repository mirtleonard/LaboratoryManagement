import unittest
from domain.problem import *
from repository.problem_repository import *

def test_add_problem():
    """
        test add problem to repository
    """
    problem_repository = Problem_Repository()
    assert problem_repository.size() == 0
    problem = Problem(1, "Sort an array", "24.11.2021")
    problem_repository.add(problem)
    assert problem_repository.size() == 1
    problem = Problem(1, 'Make sum', "23.11.2021")
    try:
        problem_repository.add(problem)
    except:
        pass
    assert problem_repository.size() == 1

def test_delete_problem():
    """
        test remove problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "Sort an array", "24.11.2021")
    problem_repository.add(problem)
    problem_repository.delete(1)
    assert problem_repository.size() == 0

def test_find_problem():
    """
        test find problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "CMMDC", "21.11.2021")
    problem_repository.add(problem)
    problem = problem_repository.find(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMDC'
    assert problem.get_deadline() == '21.11.2021'

def test_update_problem():
    """
        test update problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "CMMDC", "21.11.2021")
    problem_repository.add(problem)
    problem = Problem(1, 'CMMMC', '24.11.2021')
    problem_repository.update(1, problem)
    problem = problem_repository.find(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMMC'
    assert problem.get_deadline() == '24.11.2021'


class Test_problem_File_Repository(unittest.TestCase):
    def __setUp(self, file):
        self.__file = file
        self.__repository = Problem_File_Repository(file)
        self.__problem = Problem(1, "CMMDC", "24.11.2021")
        self.__repository.delete_all(file)

    def __test_add(self):
        self.__repository.add(self.__problem)
        assert self.__repository.find(1) == self.__problem
        test_repository = Problem_File_Repository(self.__file)
        assert test_repository.find(1) == self.__problem
        self.__repository.delete_all(self.__file)

    def __test_remove(self):
        self.__repository.add(self.__problem)
        self.__repository.delete(self.__problem.get_id())
        assert self.__repository.size() == 0
        test_repository = Problem_File_Repository(self.__file)
        assert test_repository.size() == 0
        self.__repository.delete_all(self.__file)

    def __test_update(self):
        self.__repository.add(self.__problem)
        new_problem = Problem(1, 'CMMMC', '25.11.2021')
        self.__repository.update(1, new_problem)
        assert self.__repository.find(1) == new_problem
        test_repository = Problem_File_Repository(self.__file)
        assert test_repository.find(1) == new_problem
        self.__repository.delete_all(self.__file)

    def run_tests(self):
        self.__setUp("tests/test_problem.txt")
        self.__test_add()
        self.__test_update()
        self.__test_remove()
