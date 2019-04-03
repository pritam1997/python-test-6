s = input("Enter sentence : ")

a=0
n=0
for i in s:
	if i.isalpha():
		a+=1
	if i.isnumeric():
		n+=1

print("LETTERS",a)
print("DIGITS",n)
