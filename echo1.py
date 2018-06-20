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


if __name__ == "__main__":
    main()
