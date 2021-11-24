from tests.domain.test_student import *
from tests.domain.test_problem import *
from tests.repository.test_student_repository import *

def run_tests():
    test_create_student()
    test_create_problem()
    test_add_student()
