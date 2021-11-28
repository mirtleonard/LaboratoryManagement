import unittest
from domain.student import *
from repository.student_repository import *

def test_add_student():
    """
        test if a student is added to repository
    """
    student_repository = Student_Repository()
    assert(student_repository.size() == 0)
    student = Student(1, 'Andrei', 214)
    student_repository.add(student)
    assert(student_repository.size() == 1)
    student = Student(1, 'Ion', 201)
    try:
        student_repository.add(student)
    except:
        pass
    assert(student_repository.size() == 1)

def test_delete_student():
    """
        tests remove student from repository
    """
    student_repository = Student_Repository()
    student = Student(1, 'Andrei', 214)
    student_repository.add(student)
    student_repository.delete(student.get_id())
    assert(student_repository.size() == 0)
    try:
        student_repository.delete(student.get_id())
        assert(False)
    except:
        pass

def test_find_student():
    """
        tests find student from repository
    """
    student_repository = Student_Repository()
    student = Student(1, 'Andrei', 214)
    student_repository.add(student)
    student = student_repository.find(1)
    assert student.get_id() == 1
    assert student.get_name() == 'Andrei'
    assert student.get_group() == 214
    try:
        student_repository.find(2)
        assert(False)
    except:
        pass

def test_update_student():
    """
        test update student from repository
    """
    student_repository = Student_Repository()
    student = Student(1, 'Andrei', 214)
    student_repository.add(student)
    student = Student(1, 'Ionescu', 200)
    student_repository.update(1, student)
    student = student_repository.find(1)
    assert student.get_id() == 1
    assert student.get_name() == 'Ionescu'
    assert student.get_group() == 200

class Test_Student_File_Repository(unittest.TestCase):
    def __setUp(self, file):
        self.__file = file
        self.__repository = Student_File_Repository(file)
        self.__student = Student(1, 'Andrei', 214)
        self.__repository.delete_all(file)

    def __test_add(self):
        self.__repository.add(self.__student)
        assert self.__repository.find(1) == self.__student
        test_repository = Student_File_Repository(self.__file)
        assert test_repository.find(1) == self.__student
        self.__repository.delete_all(self.__file)

    def __test_remove(self):
        self.__repository.add(self.__student)
        self.__repository.delete(self.__student.get_id())
        assert self.__repository.size() == 0
        test_repository = Student_File_Repository(self.__file)
        assert test_repository.size() == 0
        self.__repository.delete_all(self.__file)

    def __test_update(self):
        self.__repository.add(self.__student)
        new_student = Student(1, "Alin", 200)
        self.__repository.update(1, new_student)
        assert self.__repository.find(1) == new_student
        test_repository = Student_File_Repository(self.__file)
        assert test_repository.find(1) == new_student
        self.__repository.delete_all(self.__file)

    def run_tests(self):
        self.__setUp("tests/test_student.txt")
        self.__test_add()
        self.__test_update()
        self.__test_remove()
