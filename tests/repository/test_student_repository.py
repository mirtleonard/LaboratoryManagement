from domain.student import *
from repository.student_repository import *

def test_add_student():
    """
        test if a student is added to repository
    """
    student_repository = Student_Repository()
    assert(student_repository.size() == 0)
    student_repository.add_student(1, 'Andrei', 214)
    assert(student_repository.size() == 1)
    #student_repository.add_student(1, 'Ion', 201)
    #assert(student_repository.size() == 1)

def test_delete_student():
    """
        test remove student from repository
    """
    student_repository = Student_Repository()
    student_repository.add_student(1, 'Andrei', 214)
    student_repository.delete_student(1)
    assert(student_repository.size() == 0)

def test_find_student():
    """
        test find student from repository
    """
    student_repository = Student_Repository()
    student_repository.add_student(1, 'Andrei', 214)
    student = student_repository.find_student(1)
    assert student.get_id() == 1
    assert student.get_name() == 'Andrei'
    assert student.get_group() == 214

def test_update_student():
    """
        test update student from repository
    """
    student_repository = Student_Repository()
    student_repository.add_student(1, 'Andrei', 214)
    student_repository.update_student(1, 'Ionescu', 200)
    student = student_repository.find_student(1)
    assert student.get_id() == 1
    assert student.get_name() == 'Ionescu'
    assert student.get_group() == 200
