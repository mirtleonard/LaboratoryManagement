from domain.student import *

def test_create_student():
    """
    tests if new instance of student is valid
    """
    student = Student(1, 'Andrei', 214)
    assert student.get_id() == 1
    assert student.get_name() == 'Andrei'
    assert student.get_group() == 214
