from tests.run_tests import *
from ui.console import Console_UI
from repository.student_repository import *
from repository.problem_repository import *

run_tests()
student_repository = Student_Repository()
problem_repository = Problem_Repository()
ui = Console_UI(student_repository, problem_repository)
ui.read_input()
