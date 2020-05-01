import class_test
peter = class_test.BasicStaff('Peter',0)
john = class_test.ManagementStaff('John',0,1000,0)
print(peter)
print(john)
print('Peter\'s Pay = ', peter.calculatePay())
print('John\'s Pay = ', john.calculatePay())
print('John\'s Performance Bonus = ', john.calculatePerformanceBonus())
