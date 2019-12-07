"""
This module will open the text files
containing student and password list
File will be created if it doesn't
exist yet.
yeet

latter half will read and compare for
login purposes
yeet
"""


def add_suser_file(strng):
    f = open("sUser.txt", "a+")
    f.write("%s\n" % strng)
    f.close()


def add_spassword_file(strng):
    f = open("sPassword.txt", "a+")
    f.write("%s\n" % strng)
    f.close()


def login_check(email, password):
    ctr = int(0)
    ctr2 = int(0)
    with open("sUser.txt", "r") as f:
        checker = len(f.readlines())
        f.seek(0)
        for line in f:
            ctr = ctr + 1
            if email == line.strip():
                break
            elif ctr == checker:
                return 2

    with open("sPassword.txt", "r") as f2:
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
