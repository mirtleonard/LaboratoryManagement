from domain.problem import *

def test_create_problem():
    """
    tests if new instance of student is valid
    """
    problem = Problem(23, "Sorteaza crescator un array dat.", "21.11.2021")
    assert problem.get_id() == 23
    assert problem.get_description() == "Sorteaza crescator un array dat."
    assert problem.get__deadline() == "21.11.2021"
