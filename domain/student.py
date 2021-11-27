class Student:
    """
        Represent a student
        id - integer
        name - string
        group - integer
    """
    def __init__(self, id, name, group):
        """
            Create a new student with the given id, name and group
        """
        self.__id = id
        self.__name = name
        self.__group = group

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_name(self, new_name):
        self.__name = new_name

    def set_group(self, new_group):
        self.__group = new_group

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__id == other.get_id()
        return False

    def __str__(self):
        return "| ID | Name | Group |\n"  +  "_____________________\n" + str(self.__id) + " | " + self.__name + " | " + str(self.__group)

class Student_Validator:
    """
        Validates instance of a student
    """
    def validate_student(self, student):
        errors = ""
        if student.get_id() < 0:
            errors += "invalid id\n"
        if student.get_name() == "":
            errors += "invalid name\n"
        if student.get_group() < 0:
            errors += "invalid group\n"
        if len(errors) > 0:
            raise ValidationError(errors)
