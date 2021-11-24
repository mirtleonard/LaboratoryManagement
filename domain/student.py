class Student:
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

class Student_Validator:
    def validate_student(self, student):
        """
            Validates instance of a student 
        """
        errors = ""
        if student.get_id() < 0:
            errors += "invalid id\n"
        if student.get_name() == "":
            errors += "invalid name\n"
        if student.get_group() < 0:
            errors += "invalid group\n"
        if len(errors) > 0:
            raise ValidationError(errors)
