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
