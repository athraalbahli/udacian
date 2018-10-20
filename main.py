class Udacian:
	def __init__(self,name,city, enrollment, nanodegree, status):
		self.name = name
		self.city = city
		self.enrollment = enrollment
		self.nanodegree = nanodegree
		self.status = status

	def print_string(self):
		print("my name is {0} in {1} studing {2} nanodegree with Ms {3} , she is {4}" . format(self.name, self.city,self.enrollment, self.nanodegree,self.status))


athra = Udacian("Athra" , "Dammam" , "Full Stack Web Developer" , "Elham" , "on track")
athra.print_string()