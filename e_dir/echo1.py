def edit_story(words,func):
	for word in words:
		print(func(word))
def enliven(word):
	return word.capitalize() + '!'
def echo(anything):
    'echo returns its input argument'
    return(anything)


def print_if_true(thing, check):
    ''' 
            Prints the first argument if a second argument is true;
            The operation is:
                    1: Check whether the *second* argument is true.
                    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)
    return()

def answer():
    return 42


def run_something(func):
    func()
    return True


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
    return True


def add_args(arg1, arg2):
    print(arg1+arg2)
    return True

def sum_args(*args):
	return sum(args)

def run_with_positional_args(func,*args):
	return func(*args)

def outer(a,b):
	def inner(c,d):
		return c+d
	return inner(a,b)
def knights(saying):
	def inner(quote):
		return "We are the knights who say: '%s'" % quote
	return inner(saying)
def knights2(saying):
	def inner2():
		return "We are the knights who say: '%s'" % saying
	return inner2
def dummy():
	print("dummy")
def main():
    print("add_args\n")
    print(type(add_args))
    print(echo('test1'))
    print_if_true('test2', True)
    print_if_true('test3', False)
    print(echo.__doc__)
    print(print_if_true.__doc__)
    print(answer())
    run_something(answer)
    print("run_somthing\n")
    print(type(run_something))
    run_something_with_args(add_args, 5, 9)
    print("run_with_pos")
    print(run_with_positional_args(sum_args,1,2,3,4))
    print("outer run")
    print(outer(4,7))
    print("Knights")
    print(knights('Ni'))
    print(knights('cunt'))
    a = knights2('Dick')
    b = knights2('Hasenpfeffer')
    print(a)
    print(b)
    print(a())
    print(b())
    stairs = ['thud', 'meow', 'thud', 'hiss']
    edit_story(stairs,enliven)
    edit_story(stairs,lambda word: word.capitalize() + '%')
    edit_story(stairs,lambda word: word.capitalize() + '%')

    
if __name__ == "__main__":
    main()
