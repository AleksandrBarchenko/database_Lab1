from model.group import Group
from model.group_lab import GroupLab
from model.student import Student
from model.student_lab import StudentLab

from values import strings
from view import gui

__groups_lab = GroupLab()
__students_lab = StudentLab()


def main():
    gui.clean()
    __menu()


def __validate_int(data):
    while 1:
        try:
            if len(data) > 0:
                int(data)
                return 1
            else:
                print strings.wrong_input
            return 0
        except ValueError:
            print(strings.wrong_input)
            return 0


def __add_producer():
    gui.print_title_new_group()

    name = gui.input_data(strings.input_name)

    __groups_lab.add_group(Group(name=name))


def __add_student():
    gui.print_title_new_student()

    name = gui.input_data(strings.input_name)
    age = gui.input_data(strings.input_age)

    __show_groups()

    res = 0
    while not res:
        group_id = raw_input(strings.input_group_id)
        res = __validate_int(group_id)
        if res:
            if not __groups_lab.get_groups().has_key((int(group_id))):
                print strings.wrong_input
                res = 0

    __students_lab.add_student(Student(name=name, age=age, group_id=group_id))


def __show_groups():
    data = __groups_lab.get_groups()

    gui.print_title_groups()
    for key in data:
        gui.print_groups(data[key])


def __show_students():
    data = __students_lab.get_students()

    gui.print_title_students()
    for key in data:
        gui.print_student(data[key])


def __del_group():
    res = 0
    _id = 0
    while not res:
        _id = raw_input(strings.input_id)
        res = __validate_int(_id)

    try:
        students_ids = []
        group_data = __students_lab.get_students()
        for key in group_data.keys():
            if group_data[key].get_group_id() == _id:
                students_ids.append(key)

        for student_id in students_ids:
            __students_lab.del_student(student_id)

        __groups_lab.del_group(_id)
        return 1
    except KeyError:
        return 0


def __del_student():
    res = 0
    _id = 0
    while not res:
        _id = raw_input(strings.input_id)
        res = __validate_int(_id)

    try:
        __students_lab.del_student(int(_id))
        return 1
    except KeyError:
        return 0


def __search():
    res = 0

    __show_groups()

    while not res:
        group_id = raw_input(strings.input_id)
        res = __validate_int(group_id)
        if res:
            if not __groups_lab.get_groups().has_key(int(group_id)):
                print strings.wrong_input
                res = 0
            else:
                group = __groups_lab.get_groups().get(int(group_id))
                data = __students_lab.get_students()
                youngest = 0
                for key in data.keys():
                    if int(data[key].get_group_id()) == int(group.get_id()):
                        if youngest == 0:
                            youngest = data[key]
                        if data[key].get_age() < youngest.get_age():
                            youngest = data[key]

                if youngest != 0:
                    gui.clean()
                    gui.print_title_students()
                    gui.print_student(youngest)
                    return
                else:
                    print strings.error_student_not_found


def __change_group():
    res = 0

    __show_groups()

    while not res:
        group_id = raw_input(strings.input_id)
        res = __validate_int(group_id)
        if res:
            if not __groups_lab.get_groups().has_key(int(group_id)):
                print strings.wrong_input
                res = 0
            else:
                group = __groups_lab.get_groups().get(int(group_id))
                gui.clean()

                while 1:
                    gui.print_group_change_menu()
                    choices_menu = raw_input(strings.choice_hint)
                    try:
                        choices_menu = int(choices_menu)
                        if choices_menu == 1:
                            gui.clean()
                            group.set_name(raw_input(strings.input_name))
                            gui.successful_message()
                            continue
                        elif choices_menu == 2:
                            gui.clean()
                            break
                        else:
                            print(strings.wrong_input)
                    except ValueError:
                        print(strings.wrong_input)


def __change_student():
    res = 0

    __show_students()

    while not res:
        student_id = raw_input(strings.input_id)
        res = __validate_int(student_id)
        if res:
            if not __students_lab.get_students().has_key(int(student_id)):
                print strings.wrong_input
                res = 0
            else:
                student = __students_lab.get_students().get(int(student_id))
                gui.clean()

                while 1:
                    gui.print_student_change_menu()
                    choices_menu = raw_input(strings.choice_hint)
                    try:
                        choices_menu = int(choices_menu)
                        if choices_menu == 1:
                            gui.clean()
                            student.set_name(raw_input(strings.input_name))
                            gui.successful_message()
                            continue
                        elif choices_menu == 2:
                            gui.clean()
                            student.set_age(raw_input(strings.input_age))
                            gui.successful_message()
                            continue
                        elif choices_menu == 3:
                            gui.clean()
                            __show_groups()
                            student.set_group_id(raw_input(strings.input_group_id))
                            gui.successful_message()
                            continue
                        elif choices_menu == 4:
                            gui.clean()
                            break
                        else:
                            print(strings.wrong_input)
                    except ValueError:
                        print(strings.wrong_input)


def __menu():
    gui.print_menu()
    while 1:
        choices = raw_input(strings.choice_hint)
        try:
            choices = int(choices)
            if choices == 1:
                gui.clean()
                __add_producer()
                gui.successful_message()
                __menu()
                break
            elif choices == 2:
                gui.clean()
                if __groups_lab.size() > 0:
                    __add_student()
                    gui.successful_message()
                else:
                    gui.error_message(strings.error_add_new_student)
                __menu()
                break
            elif choices == 3:
                gui.clean()
                if __groups_lab.size() > 0:
                    __show_groups()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 4:
                gui.clean()
                if __students_lab.size() > 0:
                    __show_students()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 5:
                gui.clean()
                __search()
                gui.successful_message()
                __menu()
                break
            elif choices == 6:
                gui.clean()
                if __groups_lab.size() > 0:
                    __change_group()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 7:
                gui.clean()
                if __students_lab.size() > 0:
                    __change_student()
                    gui.successful_message()
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 8:
                gui.clean()
                if __groups_lab.size() > 0:
                    __show_groups()
                    if __del_group():
                        gui.clean()
                        __show_groups()
                        print strings.group_student_del_message
                        gui.successful_message()
                    else:
                        gui.error_message(strings.error_group_not_found)
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 9:
                gui.clean()
                if __students_lab.size() > 0:
                    __show_students()
                    if __del_student():
                        gui.clean()
                        __show_students()
                        gui.successful_message()
                    else:
                        gui.error_message(strings.error_student_not_found)
                else:
                    gui.error_message(strings.not_found_data)
                __menu()
                break
            elif choices == 0:
                __groups_lab.save_groups()
                __students_lab.save_students()
                break
            else:
                print(strings.wrong_input)
        except ValueError:
            print(strings.wrong_input)
