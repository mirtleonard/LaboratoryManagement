from domain.mark import *
from domain.problem import *
from domain.student import *
from tests.run_tests import *
from ui.console import Console_UI
from repository.mark_repository import*
from repository.student_repository import *
from repository.problem_repository import *
from controller.student_controller import *
from controller.problem_controller import *
from controller.mark_controller import *

run_tests()
#student
student_validator = Student_Validator()
#file
student_repository = Student_File_Repository("hello.txt")
#memory
student_repository = Student_Repository()
student_controller = Student_Controller(student_repository, student_validator)
#problem
problem_validator = Problem_Validator()
problem_repository = Problem_Repository()
problem_controller = Problem_Controller(problem_repository, problem_validator)
#marks
mark_validator = Mark_Validator()
mark_repository = Mark_Repository()
mark_controller = Mark_Controller(mark_repository, mark_validator)
#ui
ui = Console_UI(student_controller, problem_controller, mark_controller)
ui.read_input()
