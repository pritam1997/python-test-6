n=int(input("Enter no. : "))
s2=''
for i in range(2):
	s2=s2+str(n)

s3=''
for i in range(3):
	s3=s3+str(n)
s4=''
for i in range(4):
	s4=s4+str(n)

print(n+int(s2)+int(s3)+int(s4))