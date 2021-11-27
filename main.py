from tests.run_tests import *
from ui.console import Console_UI
from repository.mark_repository import*
from repository.student_repository import *
from repository.problem_repository import *
from controller.student_controller import *

run_tests()
student_validator = Student_Validator()
student_repository = Student_Repository()
student_controller = Student_Controller(student_repository, student_validator)

problem_repository = Problem_Repository()
mark_repository = Mark_Repository()
ui = Console_UI(student_controller, problem_repository, mark_repository)
ui.read_input()
