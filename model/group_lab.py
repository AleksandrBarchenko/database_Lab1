import pickle


class GroupLab:
    __groups_name_file = './assets/groups.txt'

    def __init__(self):
        self.__load_groups()

    def get_groups(self):
        return self.__data

    def add_group(self, producer):
        self.__data[producer.get_id()] = producer

    def del_group(self, producer_id):
        del (self.__data[int(producer_id)])

    def size(self):
        return len(self.__data)

    def save_groups(self):
        f = open(self.__groups_name_file, 'wb')
        pickle.dump(self.__data, f)
        f.close()

    def __load_groups(self):
        self.__data = {}
        try:
            f = open(self.__groups_name_file, 'rb')
            data = pickle.load(f)
            f.close()
            self.__data = data
        finally:
            return
