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
