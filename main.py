from tests.run_tests import *
from ui.console import Console_UI
from repository.mark_repository import*
from repository.student_repository import *
from repository.problem_repository import *

run_tests()
student_repository = Student_Repository()
problem_repository = Problem_Repository()
mark_repository = Mark_Repository()
ui = Console_UI(student_repository, problem_repository, mark_repository)
ui.read_input()
