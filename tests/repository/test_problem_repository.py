from domain.problem import *
from repository.problem_repository import *

def test_add_problem():
    """
        test add problem to repository
    """
    problem_repository = Problem_Repository()
    assert(problem_repository.size() == 0)
    problem_repository.add_problem(1, "Sort an array", "24.11.2021")
    assert(problem_repository.size() == 1)
