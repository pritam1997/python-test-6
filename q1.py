class Instring:
	def __init__(self,get="string"):
		self.get=get

	def getString(self):
		self.get=input("Enter string : ")

	def printString(self):
		return self.get.upper()


o=Instring()
o.getString()
print(o.printString())