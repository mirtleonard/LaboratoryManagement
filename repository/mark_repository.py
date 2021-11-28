import random
from domain.mark import *
from repository.repository_exception import *

class Mark_Repository:
    """
        Class responsible for managing a list of Mark_problem (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__marks = {}

    def add(self, student_mark):
        """
            if student_mark is valid, will add it to repository
            Mark - object of Mark type
            problem - object of Problem type
        """
        if student_mark.get_id() in self.__marks:
            raise Repository_Exception("Mark ID already exists.")
        self.__marks[student_mark.get_id()] = student_mark

    def update(self, id, new_mark):
        if not id in self.__marks:
            raise Repository_Exception("Mark with ID does't exit!")
        self.__marks[id] = new_mark

    def delete(self, id):
        """
            if id exists, will delete problem with id from repository
            id - int
        """
        if not id in self.__marks:
            raise Repository_Exception("Mark with ID does't exit!")
        del self.__marks[id]

    def find(self, id):
        """
            if mark with id exists, will be returned
            id - int
            return - Mark object
        """
        if not id in self.__marks:
            raise Repository_Exception("Mark not found!")
        return self.__marks[id]

    def get_all(self):
        """
            returns all marks from repo
        """
        return self.__marks

    def size(self):
        """
            return the number of marks in the repository
        """
        return len(self.__marks)

class Mark_File_Repository(Mark_Repository):
    def __init__(self, file, student_repository, problem_repository):
        Mark_Repository.__init__(self)
        self.__file = file
        try:
            file = open(self.__file, 'r')
        except:
            return
        line = file.readline().strip()
        while line != "":
            attrs = line.split("|")
            student = student_repository.find(int(attrs[0].strip()))
            problem = problem_repository.find(int(attrs[1].strip()))
            mark = Mark(student, problem, int(attrs[2].strip()))
            Mark_Repository.add(self, mark)
            line = file.readline().strip()
        file.close()

    def __store(self):
        file = open(self.__file, "w")
        marks = self.get_all()
        for mark in marks.values():
            file.write(str(mark) + "\n")
        file.close()

    def delete_all(self, file):
        marks = list(self.get_all().keys())
        for x in marks:
            self.delete(x)
        open(file, 'w').close()

    def add(self, mark):
        Mark_Repository.add(self, mark)
        self.__store()

    def update(self, id, new_mark):
        Mark_Repository.update(self, id, new_mark)
        self.__store()

    def delete(self, id):
        Mark_Repository.delete(self, id)
        self.__store()
