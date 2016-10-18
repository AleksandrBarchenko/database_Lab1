from values import strings
import os


def print_menu():
    print strings.menu


def print_title_new_group():
    print '\t' + strings.new_group_title


def print_title_new_student():
    print '\t' + strings.new_student_title


def print_title_groups():
    a = '|{:^8}|{:^26}|'.format(strings.id_title, strings.name_title)
    print strings.divider * len(a)
    print a
    print strings.divider * len(a)


def print_title_students():
    a = '|{:^8}|{:^26}|{:^10}|{:^13}|' \
        .format(strings.id_title, strings.name_title, strings.age_title, strings.group_id_title)
    print strings.divider * len(a)
    print a
    print strings.divider * len(a)


def print_student(student):
    a = '|{:^8}|{:^26}|{:^10}|{:^13}|' \
        .format(student.get_id(), student.get_name(), student.get_age(), student.get_group_id())
    print a
    print strings.divider * len(a)


def print_groups(producer):
    a = '|{:^8}|{:^26}|'.format(producer.get_id(), producer.get_name())
    print a
    print strings.divider * len(a)


def clean():
    os.system("cls")


def successful_message():
    raw_input(strings.successful_message)
    clean()


def error_message(error):
    raw_input(error)
    clean()


def print_group_change_menu():
    print strings.group_change_menu


def print_student_change_menu():
    print strings.student_change_menu


def input_data(string):
    res = 0
    while not res:
        data = raw_input(string)
        res = __validate(data)

    return data


def __validate(data):
    if len(data) > 0:
        return 1
    else:
        print strings.wrong_input
        return 0
