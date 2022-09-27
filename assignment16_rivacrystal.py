#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: September 29, 2021
#This program converts parsec into light years

choice = input("""Please enter the conversion you want to do:
'a' for Light-Year to Parsec conversion
'b' for Parsec to Light-Year Conversion\n""")
print(f"Your selection: {choice}")

if choice == "a":
    lightYear = float(input("Please enter the number of Light-Years: "))
elif choice == "b":
    parsec = float(input("please enter the number of Parsecs: "))

if choice == "a":
    print(f"{lightYear} Light-Years is equal to", (lightYear * 0.30660), "Parsecs.")
elif choice == "b":
    print(f"{parsec} Parsecs is equal to", (parsec * 3.2616), "Light-Years.")
