from domain.student import *
from repository.repository_exception import *

class Student_Repository:
    """
        Class responsible for managing a list of students (store, retrieve , update, etc)
        GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__students = {}

    def add(self, student):
        """
            if student is valid, will add it in respository
            student - object of type Student
        """
        if student.get_id() in self.__students:
            raise Repository_Exception("Student ID already exists.")
        self.__students[student.get_id()] = student

    def delete(self, id):
        """
            if id exists, will delete student with id from repository
            id - int
        """
        if not id in self.__students:
            raise Repository_Exception("Student with ID does't exit!")
        del self.__students[id]

    def find(self, id):
        """
            if student with id exists, will be returned
            id - integer
        """
        if not id in self.__students:
            raise Repository_Exception("Student not found!")
        return self.__students[id]

    def update(self, id, new_student):
        """
            update student with values
            id - int
            student - object of type Student
        """
        student = self.__students[id]
        self.__students[id] = new_student

    def get_all(self):
        """
            returns all students from repo
        """
        return self.__students

    def size(self):
        """
            return the number of students in the repository
        """
        return len(self.__students)

class Student_File_Repository(Student_Repository):
    def __init__(self, file):
        Student_Repository.__init__(self)
        self.__file = file
        try:
            file = open(self.__file, 'r')
        except:
            return
        line = file.readline().strip()
        while line != "":
            attrs = line.split("|")
            student = Student(int(attrs[0].strip()), attrs[1].strip(), int(attrs[2].strip()))
            Student_Repository.add(self, student)
            line = file.readline().strip()
        file.close()


    def __store(self):
        file = open(self.__file, "w")
        students = self.get_all()
        for student in students.values():
            file.write(str(student) + "\n")
        file.close()

    def delete_all(self, file):
        students = list(self.get_all().keys())
        for x in students:
            self.delete(x)
        open(file, 'w').close()

    def add(self, student):
        Student_Repository.add(self, student)
        self.__store()

    def update(self, id, new_student):
        Student_Repository.update(self, id, new_student)
        self.__store()

    def delete(self, id):
        Student_Repository.delete(self, id)
        self.__store()
