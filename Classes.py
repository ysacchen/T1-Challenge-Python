"""
6 hrs to cram w e lp
update 3.5 hrs left and only one function left
but its the most hasslest hassle ever

I feel like i couldve used an excel file
for class list and students taking it
but
1 i dont have enough time
2 i dont know if thats actually feasible
3 c l ass e s are killing me
"""
""""
Module for everything related to classes

Very messy but atm
everythings in one text file

All the classes are in one text file
students that are taking said class
have their ID written underneath the class code
with three spaces 
ex.
    GEFILI
       student1
       student2
    GEFILI2
       student1
"""


def create():
    lprereq = []
    print("What is the name of the class?")
    name = input()
    print("How many units does it have?")
    unit = int(input())
    print("How many prerequisites does it have?")
    prereqnum = int(input())
    while prereqnum != int(0):
        print("Input code of class ")
        prereq: str = input()
        lprereq.append(prereq)
        prereqnum = prereqnum - 1
    print("What is the class limit for number of students?")
    limit = int(input())
    print("What is the class code?")
    code: str = input()

    with open("Classes.txt", "a+") as f:
        f.write("%s, %s, [ " % (code.upper(), name))
        for item in lprereq:
            f.write(item)
            f.write(" ")
        f.write("], %d, %d\n" % (unit, limit))

    print("\nClass successfully added")
    return 0


def remove():
    print("Please enter the class code of")
    print("the class you want to remove")
    code: str = input()

    with open("Classes.txt", "r+") as f:
        content = f.readlines()
        f.seek(0)
        f.truncate()
        for line in content:
            if not line.startswith(code.upper(), 0, len(code)):
                f.write(line)
    print("\nClass successfully removed")
    return 0


def list_classes():
    with open("Classes.txt", "r") as f:
        for line in f:
            if not line.startswith("   "):
                print(line)

    return 0


def slist_classes(sid):

    with open("Classes.txt", "r") as f:
        ctr = int(0)
        content = f.readlines()
        f.seek(0)
        print("Code,      name      ,  prereq  , units, class limit")
        for line in content:
            ctr = ctr + 1
            if not line.startswith("   "):
                lineref = ctr
            elif line.startswith("   "):
                if line.startswith("   %s" % sid):
                    print(content[lineref -1])

    return 0


"""
this is a mess and incomplete
consider yourself warned

current problems
1. doesnt check prerequisites
2. still adds even if its already being taken
3. doesnt check capacity if the class is full
"""


def take(sid):
    print("Input the class code of the class")
    print("you wish to take")
    code: str = input()
    ctr = int(0)

    with open("Classes.txt", "r+") as f:

        content = f.readlines()
        f.seek(0)
        f.truncate()
        for line in content:
            ctr = ctr + 1
            if not line.startswith("   "):
                curr_code = line.split(', ', 1)[0]
                if curr_code.strip() == code.upper():
                    content.insert(ctr, "   %s\n" % sid)

        for line2 in content:
            f.write(line2)

    print("\nClass successfully added")
    return 0


"""
This function drop, allows students to
drop classes they're in
atm there's no error message
if the student isn't enrolled in the
class he wants to drop
"""


def drop(sid):
    print("Please enter the class code of")
    print("the class you want to drop")
    code: str = input()

    with open("Classes.txt", "r+") as f:
        ctr = int(0)
        content = f.readlines()
        f.seek(0)
        f.truncate()
        for line in content:
            ctr = ctr + 1
            if not line.startswith("   "):
                curr_code = line.split(', ', 1)[0]
                f.write(line)
            elif line.startswith("   "):
                if curr_code == code.upper():
                    if not line.startswith("   %s" % sid):
                        f.write(line)
                else:
                    f.write(line)

    print("\nClass successfully removed")
    return 0
