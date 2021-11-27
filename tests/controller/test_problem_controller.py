from controller.problem_controller import *
from repository.problem_repository import *
from domain.problem import *

def test_controller_add_problem():
    """
        tests add problem from controller
    """
    validator = Problem_Validator()
    repository = Problem_Repository()
    controller = Problem_Controller(repository, validator)
    controller.add(1, "Sort", "20/02/2022")
    problem = controller.find(1)
    assert(problem != -1)
    assert(problem.get_id() == 1)
    assert(problem.get_description() == "Sort")
    assert(problem.get_deadline() == "20/02/2022")
    try:
        controller.add(-1, "", "")
        assert(False)
    except:
        pass

def test_controller_delete_problem():
    """
        tests remove problem from controller
    """
    validator = Problem_Validator()
    repository = Problem_Repository()
    controller = Problem_Controller(repository, validator)
    controller.add(1, "Sort", "20/02/2022")
    controller.delete(1)
    try:
        controller.find(1);
        assert(False)
    except:
        pass

def test_controller_search_problem():
    """
        tests seach sutdent from controller
    """
    validator = Problem_Validator()
    repository = Problem_Repository()
    controller = Problem_Controller(repository, validator)
    controller.add(1, "Sort", "20/02/2022")
    list = controller.search("or")
    problem = Problem(1, "Sort", "20/02/2022")
    assert(list[0] == problem)
    list = controller.search("x")
    assert(list == [])

def test_controller_update_problem():
    """
        tests update sudent from controller
    """
    validator = Problem_Validator()
    repository = Problem_Repository()
    controller = Problem_Controller(repository, validator)
    controller.add(1, "Sort", "20/02/2022")
    controller.update(1, "Sum", "20/03/2022")
    problem = controller.find(1)
    assert(problem.get_id() == 1)
    assert(problem.get_description() == "Sum")
    assert(problem.get_deadline() == "20/03/2022")
    try:
        controller.update(0, "", -1)
        assert(False)
    except:
        pass

def test_controller_random_problem():
    """
        tests random problem from controller
    """
    validator = Problem_Validator()
    repository = Problem_Repository()
    controller = Problem_Controller(repository, validator)
    controller.random(10)
    assert(len(controller.search("")) == 10)
