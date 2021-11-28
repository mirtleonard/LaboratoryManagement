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

#students
student_validator = Student_Validator()
#file
student_repository = Student_File_Repository("students.txt")
#memory
#student_repository = Student_Repository()
student_controller = Student_Controller(student_repository, student_validator)

#problems
problem_validator = Problem_Validator()
#memory
#file
problem_repository = Problem_File_Repository("problems.txt")
problem_controller = Problem_Controller(problem_repository, problem_validator)

#marks
mark_validator = Mark_Validator()
#memory
#mark_repository = Mark_Repository()
#file
mark_repository = Mark_File_Repository("marks.txt", student_repository, problem_repository)
mark_controller = Mark_Controller(mark_repository, mark_validator)

#ui
ui = Console_UI(student_controller, problem_controller, mark_controller)
ui.read_input()
