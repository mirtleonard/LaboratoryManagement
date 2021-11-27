import sys
from ui.menu import *
from ui.reading import *

class Console_UI:
    """
        Class responsible with the user interface
        Will use the controller to perform operations other than read, print
    """
    def __init__(self, student_controller, problem_repository, mark_repository):
        self.__student_controller = student_controller
        self.__problem_repository = problem_repository
        self.__mark_repository = mark_repository

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
                            self.__problem_repository.add_problem(id, description, deadline)
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
                            self.__problem_repository.delete_problem(id)
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
                            print(self.__problem_repository.find_problem(id))
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
                            self.__student_controller.update(int(id), name, int(group))
                        elif options[pos + 1] == "problem":
                            id = read_input("Insert problem ID:\n>>> ", int = True)
                            description = read_input("Insert problem description:\n>>> ", string = True)
                            deadline = read_input("Insert problem deadline:\n>>> ", string = True)
                            self.__problem_repository.update_problem(id, description, deadline)
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
                            self.__problem_repository.random(entities)
                        elif options[pos + 1] == "marks":
                            entities = read_input("Insert how many entities: \n>>> ", integer = True)
                            self.__mark_repository.random(entities, self.__student_repository, self.__problem_repository)
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
                            print(self.__problem_repository)
                        elif (options[pos + 1] == "marks"):
                            print(self.__mark_repository)
                        else:
                            print("Invalid input!")
                    elif options[pos] == "assign":
                        student_id = read_input("Insert student ID:\n>>> ", integer = True)
                        problem_id = read_input("Insert problem ID:\n>>> ", integer = True)
                        mark = read_input("Insert mark:\n>>> ", integer = True)
                        self.__mark_repository.assign(student_id, problem_id, mark, self.__student_controller.get_repository(), self.__problem_repository)
                    elif options[pos] == "help":
                        help()
                    else:
                        invalid("Invalid option, type help if you are stuck!")
                except:
                    print(sys.exc_info())
