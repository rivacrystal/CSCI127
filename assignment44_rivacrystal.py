# Name: Riva Crystal
# Email: riva.crystal@gmail.com
# Date: November 9, 2021
# Correct the errors in the program to output the correct answers.

""" printUTAs(utaList) prints out every UTA on the list of UTAs alphabetically, one per line """
def printUTAs(utaList):
    print("UTA List: ")
    utaList.sort()
    for uta in utaList:
        print(uta)
    print()

""" isUTA(utaList, person) checks if the person in question is a UTA on the list and prints out a message accordingly """
def isUTA(utaList, person):
    if person in utaList:
        print(person + " is a UTA for CSci 127 Fall 2021.")
    else:
        print(person + " is not a UTA for CSci 127 Fall 2021.")

""" numUTAs(utas) return a string with how many UTAs are working this semester """
def numUTAs(utas):
    num = len(utas)
    return "There are " + str(num) + " UTAs who love helping students in CSci 127 Fall 2021."


def main():
    # A list of UTAs working this semester
    utas = ["Mandy", "Leonardo", "Nancy", "Ifte", "Aida", "Arterio", "Destiny", "Ghazanfar", "Ilya", "Sadab", "Stephanie", "Tyler"]

    printUTAs(utas)

    isUTA(utas, "Lola")
    isUTA(utas, "Mandy")
    isUTA(utas, "Leonardo")
    isUTA(utas, "Yash")

    print(numUTAs(utas))


if __name__ == '__main__':
    main()
