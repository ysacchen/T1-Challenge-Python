"""
This is for admin related files
at the moment adding new admins is not
being implemented because,,,,
reasons,,,,

"""


def add_auser_file(strng):
    f = open("aUser.txt", "a+")
    f.write("%s\n" % strng)
    f.close()


def add_apassword_file(strng):
    f = open("aPassword.txt", "a+")
    f.write("%s\n" % strng)
    f.close()


def login_check(email, password):
    ctr = int(0)
    ctr2 = int(0)
    with open("aUser.txt", "r") as f:
        checker = len(f.readlines())
        f.seek(0)
        for line in f:
            ctr = ctr + 1
            if email == line.strip():
                break
            elif ctr == checker:
                return 2

    with open("aPassword.txt", "r") as f2:
        for i in f2:
            ctr2 = ctr2 + 1
            if ctr2 == ctr:
                if i.strip() == password:
                    return 1
                else:
                    return 2
            elif ctr2 >= ctr:
                return 2

    return 0
