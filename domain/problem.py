class Problem:
    def __init__(self, id, description, deadline):
        """
            Create a new problem with given id, description, deadline
            id - int
            description - string
            deadline - string
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

    def __eq__(self, other):
        if isinstance(other, Problem):
            return self.__id == other.get_id()
        return False

    def __str__(self):
        return str(self.__id) + " | " + self.__description + " | " + str(self.__deadline)

class Problem_Validator:
    def validate(self, problem):
        """
            Validates instance of a problem
        """
        errors = ""
        if problem.get_id() < 0:
            errors += "invalid id\n"
        if problem.get_description() == "":
            errors += "invalid name\n"
        if problem.get_deadline() == "":
            errors += "invalid deadline\n"
        if len(errors) > 0:
            raise ValidationError(errors)
