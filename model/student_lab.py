import pickle


class StudentLab:
    __students_name_file = './assets/students.txt'

    def __init__(self):
        self.__load_students()

    def get_students(self):
        return self.__data

    def add_student(self, film):
        self.__data[film.get_id()] = film

    def del_student(self, film_id):
        del (self.__data[int(film_id)])

    def size(self):
        return len(self.__data)

    def save_students(self):
        f = open(self.__students_name_file, 'wb')
        pickle.dump(self.__data, f)
        f.close()

    def __load_students(self):
        self.__data = {}
        try:
            f = open(self.__students_name_file, 'rb')
            self.__data = pickle.load(f)
            f.close()
        finally:
            return
