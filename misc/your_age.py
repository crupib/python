import datetime
def print_age(year_born):
	count = 0
	this_year = datetime.datetime.now()
	for i in range(year_born,this_year.year):
		count = count + 1
	print("You are {} years old".format(count))
year_born = 0
print("Enter your year born: ")
year_born = int(input())
print_age(year_born)
