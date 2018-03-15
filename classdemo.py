class Staff:
 def __init__ (self, pPosition, pName, pPay):
	 self.position = pPosition
	 self.name = pName
	 self.pay = pPay
	 print('Creating Staff object')
 def __str__(self): 
	 return "Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay) 
 def calculatePay(self):
	 prompt = '\nEnter number of hours worked for %s: ' %(self.name)
	 hours = input(prompt)
	 prompt = 'Enter the hourly rate for %s: ' %(self.name)
	 hourlyRate = input(prompt)
	 self.pay = int(hours)*int(hourlyRate)
	 return self.pay
class ManagementStaff(Staff):
	def __init__ (self, pName, pPay, pAllowance, pBonus):
		super().__init__('Manager',pName,pPay)
		self.allowance = pAllowance
		self.bonus = pBonus	
	def calculatePay(self):
		basicPay = super().calculatePay()
		self.pay = basicPay + self.allowance
		return self.pay
	def calculatePerformanceBonus(self):
		prompt = 'Enter performance grade for %s: ' %(self.name)
		grade = input(prompt)
		if (grade == 'A'):
			self.bonus = 1000
		else:
			self.bonus = 0
		return self.bonus
class BasicStaff(Staff):
	def __init__(self,pName,pPay):
		super().__init__('Basic',pName,pPay)

