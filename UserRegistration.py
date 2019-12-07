import StudentFiles
import AdminFiles
import StudentHP
import AdminHP


def register():
    print("\nPlease input your your email address")
    user_email: str = input()
    print("Please input password")
    user_password: str = input()
    print("\nIs email :", user_email)
    print("and password :", user_password, "correct? (Y/N)")
    user_confirm: str = input()

    if user_confirm == 'Y' or user_confirm == 'y':
        print("Congrats! Your student account is made")
        StudentFiles.add_suser_file(user_email)
        StudentFiles.add_spassword_file(user_password)
    elif user_confirm == 'N' or user_confirm == 'n':
        print("Would you like to try again? (Y/N)")
        user_confirm = input()
        if user_confirm == 'Y' or user_confirm == 'y':
            register()
        elif user_confirm == 'N' or user_confirm == 'n':
            return 0
        else:
            print("Please input a proper value")
    else:
        print("Please input a proper value")
        register()


def login(strng):
    print("Please input your your ID Number")
    input_id: str = input()
    print("Please input password")
    input_password: str = input()

    if strng == "s":
        result: int = StudentFiles.login_check(input_id, input_password)
    elif strng == "a":
        result: int = AdminFiles.login_check(input_id, input_password)
    else:
        print("Unknown error, please try again")
        return

    if result == int(1):
        print("\nLogin successful! going to homepage...")
        if strng == "s":
            StudentHP.main(input_id)
        elif strng == "a":
            AdminHP.main()
        else:
            print("Unknown error, please try again")
            return

    elif result == int(2):
        print("\nLogin credentials do not match")
        print("Please try again")
    else:
        print("\nUnknown error, try again")
        return
