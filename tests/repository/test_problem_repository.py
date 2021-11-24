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
    #problem_repository.add_problem(1, 'Make sum', "24.11.2021")
    #assert(problem_repository.size() == 1)

def test_delete_problem():
    """
        test remove problem from repository
    """
    problem_repository = Problem_Repository()
    problem_repository.add_problem(1, "CMMDC", '21.11.2021')
    problem_repository.delete_problem(1)
    assert(problem_repository.size() == 0)

def test_find_problem():
    """
        test find problem from repository
    """
    problem_repository = Problem_Repository()
    problem_repository.add_problem(1, 'CMMDC', '21.11.2021')
    problem = problem_repository.find_problem(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMDC'
    assert problem.get_deadline() == '21.11.2021'

def test_update_problem():
    """
        test update problem from repository
    """
    problem_repository = Problem_Repository()
    problem_repository.add_problem(1, 'CMMDC', '21.11.2021')
    problem_repository.update_problem(1, 'CMMMC', '24.11.2021')
    problem = problem_repository.find_problem(1)
    assert problem.get_id() == 1
    assert problem.get_description() == 'CMMMC'
    assert problem.get_deadline() == '24.11.2021'
