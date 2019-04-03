def inputInteger():
	s=input("Enter Integral numbers : ")
	sum=0
	for i in s:
		sum+=int(i)
	return sum

print(inputInteger())