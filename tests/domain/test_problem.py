from domain.problem import *

def test_create_problem():
    """
    tests if new instance of problem is valid
    """
    problem = Problem(23, "Sort in ascending order an given array.", "21.11.2021")
    assert problem.get_id() == 23
    assert problem.get_description() == "Sort in ascending order an given array."
    assert problem.get_deadline() == "21.11.2021"
