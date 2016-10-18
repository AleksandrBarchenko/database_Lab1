class Student:
    def __init__(self, name, age, group_id):
        self.__id = id(self)
        self.__name = name
        self.__age = age
        self.__group_id = group_id

    def get_id(self):
        return self.__id

    def set_id(self, _id):
        self.__id = _id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_group_id(self):
        return self.__group_id

    def set_group_id(self, group_id):
        self.__group_id = group_id
