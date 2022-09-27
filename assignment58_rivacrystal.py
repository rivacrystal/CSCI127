num = int(input("Please enter a number: "))
sym = input("Please enter a character: ")
print("\n")
x = 0

while x < num:
	print(sym*x)
	x += 1

for i in range(num+1):
	print(sym*num)