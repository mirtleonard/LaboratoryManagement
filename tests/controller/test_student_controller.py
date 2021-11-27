from controller.student_controller import *
from repository.student_repository import *
from domain.student import *

def test_controller_add_student():
    """
        tests add student from controller
    """
    validator = Student_Validator()
    repository = Student_Repository()
    controller = Student_Controller(repository, validator)
    controller.add(1, "Alin", 204)
    student = controller.find(1)
    assert(student != -1)
    assert(student.get_id() == 1)
    assert(student.get_name() == "Alin")
    assert(student.get_group() == 204)
    try:
        controller.add(-1, "", -12)
        assert(False)
    except:
        pass

def test_controller_delete_student():
    """
        tests remove student from controller
    """
    validator = Student_Validator()
    repository = Student_Repository()
    controller = Student_Controller(repository, validator)
    controller.add(1, "Alin", 204)
    controller.delete(1)
    assert(controller.find(1) == -1)

def test_controller_search_student():
    """
        tests seach sutdent from controller
    """
    validator = Student_Validator()
    repository = Student_Repository()
    controller = Student_Controller(repository, validator)
    controller.add(1, "Alin", 204)
    list = controller.search("li")
    student = Student(1, "Alin", 204)
    assert(list[0] == student)
    list = controller.search("x")
    assert(list == [])

def test_controller_update_student():
    """
        tests update sudent from controller
    """
    validator = Student_Validator()
    repository = Student_Repository()
    controller = Student_Controller(repository, validator)
    controller.add(1, "Alin", 204)
    controller.update(1, "Ion", 210)
    student = controller.find(1)
    assert(student.get_id() == 1)
    assert(student.get_name() == "Ion")
    assert(student.get_group() == 210)
    try:
        controller.update(0, "", -1)
        assert(False)
    except:
        pass

def test_controller_random_student():
    """
        tests random student from controller
    """
    validator = Student_Validator()
    repository = Student_Repository()
    controller = Student_Controller(repository, validator)
    controller.random(10)
    assert(len(controller.search("")) == 10)
