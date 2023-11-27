class ProgStaff:
	companyName = 'ProgrammingSchool'
	def __init__(self,pSalary):
		self.salary = pSalary
	def printInfo(self):
		print("Company name is", ProgStaff.companyName)
		print("Salary is", self.salary)
peter = ProgStaff(2500)
john  = ProgStaff(2500)
print(peter.companyName)
print(john.companyName)
peter.salary = 2700
print(peter.salary)
print(john.salary)
ProgStaff.printInfo(john)

