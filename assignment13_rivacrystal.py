# Name: Riva Crystal
# Email: riva.crystal@gmail.com
# Date: September 21, 2021
# This program splits a string of books

answer = input("Enter a list of books and their authors:")
books = answer.split(";")

for i in range(len(books)):
    books[i] = books[i].split("-")


for i in range(len(books)):
    books[i][1] = books[i][1].split()[0][0] + "." + books[i][1].split()[1][0]

for i in books:
    print(i[0].lstrip() + "by " + i[1] + ".")

print("Thank you for using my book organizer!")
