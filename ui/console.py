from ui.menu import *
from ui.reading import *

class Console_UI:
    """
        Class responsible with the user interface
        Will use the controller to perform operations other than read, print
    """
    def __init__(self, student_repository, problem_repository):
        self.__student_repository = student_repository
        self.__problem_repository = problem_repository

    def read_input(self):
        while True:
            skip = 0
            options = read_input(">>> ")
            options = options.split()
            for pos in range(len(options)):
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
                        self.__student_repository.add_student(id, name, group)
                    elif options[pos + 1] == "problem":
                        id = read_input("Insert problem ID:\n>>> ", integer = True)
                        description = read_input("Insert problem description:\n>>> ", string = True)
                        deadline = read_input("Insert problem deadline:\n>>> ", string = True)
                        self.__problem_repository.add_problem(id, description, deadline)
                elif options[pos] == "remove":
                    if (len(options) <= pos + 1):
                        continue
                    skip += 1
                    if options[pos + 1] == "student":
                        id = read_input("Insert the student id\n>>> ", integer=True)
                        self.__student_repository.delete_student(id)
                    elif options[pos + 1] == "problem":
                        id = read_input("Insert the problem id\n>>> ", integer=True)
                        self.__problem_repository.delete_problem(id)
                    else:
                        invalid()
                elif options[pos] == "find":
                    if (len(options) <= pos + 1):
                        continue
                    skip += 1
                    if options[pos + 1] == "student":
                        id = read_input("Insert the student id\n>>> ", integer=True)
                        print(self.__student_repository.find_student(id))
                    elif options[pos + 1] == "problem":
                        id = read_input("Insert the problem id\n>>> ", integer=True)
                        print(self.__problem_repository.find_problem(id))
                    else:
                        invalid()
                elif options[pos] == "update":
                    if (len(options) <= pos + 1):
                        continue
                    skip += 1
                    if options[pos + 1] == "student":
                        id = read_input("Insert student ID:\n>>> ", integer = True)
                        name = read_input("Insert student new name:\n>>> ", string = True)
                        group = read_input("Insert student new group:\n>>> ", integer = True)
                        self.__student_repository.update_student(int(id), name, int(group))
                    elif options[pos + 1] == "problem":
                        id = read_input("Insert problem ID:\n>>> ", int = True)
                        description = read_input("Insert problem description:\n>>> ", string = True)
                        deadline = read_input("Insert problem deadline:\n>>> ", string = True)
                        self.__problem_repository.update_problem(id, description, deadline)
                    else:
                        invalid()
                elif options[pos] == "show":
                    if (len(options) <= pos + 1):
                        continue
                    skip += 1
                    if (options[pos + 1] == "students"):
                        print(self.__student_repository)
                    elif (options[pos + 1] == "problems"):
                        print(self.__problem_repository)
                    else:
                        print("Invalid input!")
                elif options[pos] == "help":
                    help()
                else:
                    invalid("Invalid option, type help if you are stuck!")
