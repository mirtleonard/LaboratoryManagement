def problem_top_students(marks_controller, problem):
    marks = marks_controller.search_by_problem(problem.get_id())
    marks.sort(key = lambda mark : mark.get_student().get_name())
    marks.sort(key = lambda mark : mark.get_mark(), reverse = True)
    return marks

def students_who_failed(marks_controller, students):
    result = []
    for student in students:
        marks = marks_controller.search_by_student(student.get_id())
        sum = 0
        for mark in marks:
            sum += mark.get_mark()
        average = sum / len(marks)
        if average < 5:
            result.append([student, average])
    return result

def top_50_problems(mark_controller, problems):
    assigners = {}
    result = []
    for problem in problems:
        marks = mark_controller.search_by_problem(problem.get_id())
        assigners[problem.get_id()] = len(marks)
    problems.sort(key = lambda problem : assigners[problem.get_id()], reverse = True)
    for i in range(int(len(problems) / 2)):
        result.append([problems[i], assigners[problems[i].get_id()]])
    return result
