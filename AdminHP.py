
import Classes


def main():
    print("\nWelcome, what would you like to do")
    print("1 Create a class")
    print("2 Remove a class")
    print("3 List down all current classes")
    print("4 exit")

    admin_input = int(input())
    if admin_input == int(1):
        Classes.create()
    elif admin_input == int(2):
        Classes.remove()
    elif admin_input == int(3):
        Classes.list_classes()
    elif admin_input == int(4):
        return
    else:
        print("Please input a valid value")

    main()
