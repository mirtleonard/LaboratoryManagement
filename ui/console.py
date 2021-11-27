import sys
from ui.menu import *
from ui.reading import *
from controller.statistics import *

class Console_UI:
    """
        Class responsible with the user interface
        Will use the controller to perform operations other than read, print
    """
    def __init__(self, student_controller, problem_controller, mark_controller):
        self.__student_controller = student_controller
        self.__problem_controller = problem_controller
        self.__mark_controller = mark_controller

    def read_input(self):
        while True:
            skip = 0
            options = read_input(">>> ")
            options = options.split()
            for pos in range(len(options)):
                try:
                    if skip > 0:
                        skip -= 1
                        continue
                    if options[pos] == "exit":
                        return
                    elif options[pos] == "add":
                        if (len(options) <= pos + 1):
                            continue
                        skip += 1
                        if options[pos + 1] == "student":
                            id = read_input("Insert student ID:\n>>> ", integer = True)
                            name = read_input("Insert student name:\n>>> ", string = True)
                            group = read_input("Insert student group:\n>>> ", integer = True)
                            self.__student_controller.add(id, name, group)
                        elif options[pos + 1] == "problem":
                            id = read_input("Insert problem ID:\n>>> ", integer = True)
                            description = read_input("Insert problem description:\n>>> ", string = True)
                            deadline = read_input("Insert problem deadline:\n>>> ", string = True)
                            self.__problem_controller.add(id, description, deadline)
                        elif options[pos + 1] == "mark":
                            student_id = read_input("Insert student ID:\n>>> ", integer = True)
                            problem_id = read_input("Insert problem ID:\n>>> ", integer = True)
                            mark = read_input("Insert mark:\n>>> ", integer = True)
                            self.__mark_controller.add(student_id, problem_id, mark, self.__student_controller.get_repository(), self.__problem_controller.get_repository())
                        else:
                            invalid()
                    elif options[pos] == "remove":
                        if (len(options) <= pos + 1):
                            continue
                        skip += 1
                        id = read_input("Insert the id(integer > 0)\n>>> ", integer=True)
                        if options[pos + 1] == "student":
                            self.__student_controller.delete(id)
                        elif options[pos + 1] == "problem":
                            self.__problem_controller.delete(id)
                        else:
                            invalid()
                    elif options[pos] == "find":
                        if (len(options) <= pos + 1):
                            continue
                        skip += 1
                        id = read_input("Insert id(integer > 0)\n>>> ", integer=True)
                        if options[pos + 1] == "student":
                            print(self.__student_controller.find(id))
                        elif options[pos + 1] == "problem":
                            print(self.__problem_controller.find(id))
                        else:
                            invalid()
                    elif options[pos] == "update":
                        if len(options) <= pos + 1:
                            continue
                        skip += 1
                        if options[pos + 1] == "student":
                            id = read_input("Insert student ID:\n>>> ", integer = True)
                            name = read_input("Insert student new name:\n>>> ", string = True)
                            group = read_input("Insert student new group:\n>>> ", integer = True)
                            self.__student_controller.update(id, name, group)
                        elif options[pos + 1] == "problem":
                            id = read_input("Insert problem ID:\n>>> ", int = True)
                            description = read_input("Insert problem description:\n>>> ", string = True)
                            deadline = read_input("Insert problem deadline:\n>>> ", string = True)
                            self.__problem_controller.update(id, description, deadline)
                        else:
                            invalid()
                    elif options[pos] == "random":
                        if len(options) <= pos + 1:
                            continue
                        skip += 1
                        if options[pos + 1] == "students":
                            entities = read_input("Insert how many entities: \n>>> ", integer = True)
                            self.__student_controller.random(entities)
                        elif options[pos + 1] == "problems":
                            entities = read_input("Insert how many entities: \n>>> ", integer = True)
                            self.__problem_controller.random(entities)
                        elif options[pos + 1] == "marks":
                            entities = read_input("Insert how many entities: \n>>> ", integer = True)
                            self.__mark_controller.random(entities, self.__student_controller.get_repository().get_all(), self.__problem_controller.get_repository().get_all())
                        else:
                            invalid()
                    elif options[pos] == "show":
                        if (len(options) <= pos + 1):
                            continue
                        skip += 1
                        if (options[pos + 1] == "students"):
                            students = self.__student_controller.search("")
                            print("| ID | Name | Group |\n"  +  "_____________________\n")
                            for student in students:
                                print(student)
                        elif (options[pos + 1] == "problems"):
                            problems = self.__problem_controller.search("")
                            print("| ID | Description | Deadline |\n"  +  "_______________________________\n")
                            for problem in problems:
                                print(problem)
                        elif (options[pos + 1] == "marks"):
                            marks = self.__mark_controller.search_by_problem("")
                            print("| Student | Problem | Mark |\n____________________________\n")
                            for mark in marks:
                                print(mark)
                        else:
                            invalid()
                    elif options[pos] == "statistics":
                        statistics_menu()
                        option = read_input("Enter the number of the option\n>>> ", integer = True)
                        if option == 1:
                            id = read_input("Insert the problem id \n>>> ", integer = True)
                            problem = self.__problem_controller.find(id)
                            marks = problem_top_students(self.__mark_controller, problem)
                            print("| Student | Problem | Mark |\n____________________________\n")
                            for mark in marks:
                                print(mark)
                        elif option == 2:
                            students = students_who_failed(self.__mark_controller, self.__student_controller.search(""))
                            print("| Student ID | Student Name | Student Group | Average |\n_______________________________________________________")
                            for student in students:
                                print(student[0], "|", student[1])
                        elif option == 3:
                            problems = top_50_problems(self.__mark_controller, self.__problem_controller.search(""))
                            print("| Problem ID | Problem Description | Problem Deadline | Assigners |\n___________________________________________________________________\n")
                            for problem in problems:
                                print (problem[0], "|", problem[1])
                        else:
                            invalid()
                    elif options[pos] == "help":
                        help_menu()
                    else:
                        invalid("Invalid option, type help if you are stuck!")
                except:
                    invalid(sys.exc_info()[1])
