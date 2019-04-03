"""Compare length of 2 string"""
def stringfunc():
	print(__doc__)
	s1=input("Enter 1st string : ")
	s2=input("Enter 2nd string : ")

	if len(s1)>len(s2):
		print(s1)
	elif len(s1) == len(s2):
		print(s1)
		print(s2)
	else:
		print(s2)


stringfunc()