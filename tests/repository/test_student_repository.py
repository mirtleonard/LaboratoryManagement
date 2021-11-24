from domain.student import *
from repository.student_repository import *

def test_add_student():
    """
        tests if a student is added to repository
    """
    student_repository = Student_Repository()
    assert(student_repository.size() == 0)
    student_repository.add_student(1, 'Andrei', 214)
    assert(student_repository.size() == 1)
    #student_repository.add_student(1, 'Ion', 201)
    #assert(student_repository.size() == 1)
