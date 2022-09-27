# Name: Riva Crystal
# Email: riva.crystal@gmail.com
# Date: September 16, 2021
# This program shifts a message by 5

message = (input("Enter a message:"))

for x in message:
 print(x, "shifted by 5 characters is:", chr(ord(x)+5))
