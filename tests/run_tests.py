from tests.domain.test_student import *
from tests.domain.test_problem import *
from tests.repository.test_student_repository import *
from tests.repository.test_problem_repository import *
from tests.controller.test_student_controller import *
from tests.controller.test_problem_controller import *

def run_tests():
    #student class
    test_create_student()
    #student repository
    test_add_student()
    test_delete_student()
    test_find_student()
    test_update_student()
    Test_Student_File_Repository().run_tests()
    #student controller
    test_controller_add_student()
    test_controller_delete_student()
    test_controller_random_student()
    test_controller_search_student()
    test_controller_update_student()
    #problem class
    test_create_problem()
    #problem controller()
    test_controller_add_problem()
    test_controller_delete_problem()
    test_controller_search_problem()
    test_controller_random_problem()
    test_controller_update_problem()
    #problem repository
    test_add_problem()
    test_delete_problem()
    test_find_problem()
    test_update_problem()
    Test_problem_File_Repository().run_tests()
