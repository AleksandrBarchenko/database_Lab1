class Group:
    def __init__(self, name):
        self.__id = id(self)
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
