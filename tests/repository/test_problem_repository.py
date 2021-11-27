from domain.problem import *
from repository.problem_repository import *

def test_add_problem():
    """
        test add problem to repository
    """
    problem_repository = Problem_Repository()
    assert problem_repository.size() == 0
    problem = Problem(1, "Sort an array", "24.11.2021")
    problem_repository.add(problem)
    assert problem_repository.size() == 1
    problem = Problem(1, 'Make sum', "23.11.2021")
    try:
        problem_repository.add(problem)
    except:
        pass
    assert problem_repository.size() == 1

def test_delete_problem():
    """
        test remove problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "Sort an array", "24.11.2021")
    problem_repository.add(problem)
    problem_repository.delete(1)
    assert problem_repository.size() == 0

def test_find_problem():
    """
        test find problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "CMMDC", "21.11.2021")
    problem_repository.add(problem)
    problem = problem_repository.find(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMDC'
    assert problem.get_deadline() == '21.11.2021'

def test_update_problem():
    """
        test update problem from repository
    """
    problem_repository = Problem_Repository()
    problem = Problem(1, "CMMDC", "21.11.2021")
    problem_repository.add(problem)
    problem = Problem(1, 'CMMMC', '24.11.2021')
    problem_repository.update(1, problem)
    problem = problem_repository.find(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMMC'
    assert problem.get_deadline() == '24.11.2021'
