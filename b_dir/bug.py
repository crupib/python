def hello(passname):
	"""Great everyone."""
	print(f"Hello, {passname}!")
def post_msg(user,*msgs):
	"""Post a message from a user."""
	print(f"{user}: said:")
	for msg in msgs:
		print(f"  {msg}")
def post_msg_kw(user,msg):
	"""Post a message from a user."""
	print(f"{user}: said: {msg}")
def desc_user(user, **desc):
	"""Describe a user."""
	print(f"Description of {user}:")
	for key, value in desc.items():
		print(f"  {key}: {value}")
def coffee(size=12):
	"""Server a cup of coffee,"""
	if size == 20:
		print(f"Here's your venti coffee!")
	else:
		print(f"Here's your {size} oz coffee!")
bugs = ['bug 1', 'bug 2', 'bug 3']
#while bugs:
#    bug = bugs.pop(0)
#    print(f"Fixing {bug}.")
#print("All bugs fixed")
#while True:
#    name = input("What's your name? ")
#    if name =='quit':
#      break
#    print(f"Hello, {name}!")
#while True:
#    age = input("How old are you? ")
#    age = int(age)
#    if age < 0:
#      print("Fucker")
#      continue
#    if age == 999:
#      break
#    else:
#       print(f"({age} is a great age!")
#hello("Gretchen whore")    
#post_msg("Gretchen","I love to give bj's!")
#post_msg("Bill","I love to get blow jobs from Gretchen the whore!","hard cock!","suck my ass")
#post_msg_kw(user="Willie",msg="Fuck off")
#desc_user('anton', active=True, email="anton@fuck.com",num_posts=578)
coffee()
coffee(20)
