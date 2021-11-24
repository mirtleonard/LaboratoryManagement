class Repository_Exception(Exception):
    """
      Base class for the exceptions in the repository
    """
    def __init__(self, msg):
        self.__msg = msg
    def get_msg(self):
        return self.__msg
    def __str__(self):
        return self.__msg
