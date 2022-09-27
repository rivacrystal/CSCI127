# Name: Riva Crystal
# Email: riva.crystal@gmail.com
# Date: September 16, 2021
# This program reverses words, etc.

phrase = input("Enter a phrase:")
riva = phrase[::-1]
print(riva)

riva = riva.upper()
riva = riva.split()

dun = ""

for x in riva:
    dun = dun + x[-1]

print(dun)
