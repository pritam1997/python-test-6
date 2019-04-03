t = (1,2,3,4,5,6,7,8,9,10)
for i in range(1,len(t)+1):
	if i <= len(t)/2:
		print(i,end=" ")
		if i == len(t)/2:
			print()
	elif i > len(t)/2:
		print(i,end=" ")
