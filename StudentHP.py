"""
This is the homepage module

fml let's just do our best I guess
"""
import Classes


def main(name):
    print("\nWelcome to the student homepage")
    print("1 Take a class")
    print("2 Drop a class")
    print("3 List down current classes")
    print("4 List down all classes")
    print("5 exit")

    student_input = int(input())

    if student_input == int(1):
        Classes.take(name)
    elif student_input == int(2):
        Classes.drop(name)
    elif student_input == int(3):
        Classes.slist_classes(name)
    elif student_input == int(4):
        Classes.list_classes()
    elif student_input == int(5):
        return
    else:
        print("Please input a valid value")

    main(name)
