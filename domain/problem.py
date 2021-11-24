class Problem:
    def __init__(self, id, description, deadline):
        """
            Create a new problem with given id, description, deadline
        """
        self.__id = id
        self.__description = description
        self.__deadline = deadline

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_deadline(self, new_deadline):
        self.__deadline = new_deadline

    def set_description(self, new_description):
        self.__description = new_description
