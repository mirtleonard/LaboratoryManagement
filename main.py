from domain.problem import *
from domain.student import *
from tests.run_tests import *
from ui.console import Console_UI
from repository.mark_repository import*
from repository.student_repository import *
from controller.student_controller import *
from repository.problem_repository import *
from controller.problem_controller import *

run_tests()
#student
student_validator = Student_Validator()
student_repository = Student_Repository()
student_controller = Student_Controller(student_repository, student_validator)
#problem
problem_validator = Problem_Validator()
problem_repository = Problem_Repository()
problem_controller = Problem_Controller(problem_repository, problem_validator)
#marks
mark_repository = Mark_Repository()
ui = Console_UI(student_controller, problem_controller, mark_repository)
ui.read_input()
