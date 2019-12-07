# By Ysabelle Chen, WHy am i doing this Time to cram a m p


import UserRegistration


def main():
    print("\nWelcome to the enlistment System!")
    print("1 Login as a student")
    print("2 Register as a new student")
    print("3 Login as an admin")
    print("4 exit program")

    Uinput = int(input())

    if Uinput == int(1):
        print("Proceeding to login page...\n")
        UserRegistration.login("s")
        main()
    elif Uinput == int(2):
        print("Proceeding to Student Registration page...\n")
        UserRegistration.register()
        main()
    elif Uinput == int(3):
        print("Proceeding to admin login page...\n")
        UserRegistration.login("a")
        main()
    elif Uinput == int(4):
        exit()
    else:
        print("Please input a valid number")


main()