brand = 'Apple'

exchangeRate = 1.235235245

message = 'The price of this %s laptop is %4.2f USD and the exchange rate is %4.2f USD to 1 EUR' % (brand,1299,exchangeRate)

print (message)

message1 = '{0} is easier than {1}'.format('Python','Java')
message2 = '{1} is easier than {0}'.format('Python','Java')
message3 = '{:10.2f} and {:d}'.format(1.234234234,12)
message4 = '{}'.format(1.234234234)
print(message1)
print(message2)
print(message3)
print(message4)
