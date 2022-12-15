import argparse 
import datetime as dt 

def cli(): 
    parser = argparse.ArgumentParser(description='Simple Example')
    parser.add_argument('-n', '--name', type=str, 
                        default='Bill', help="Name of user") 
    parser.add_argument('-a', '--age', type=int, default=67,
                        help="Age of user") 
    parser.add_argument('-o', '--occupation', type=str,
                       default='Automation developer',
                       help='Occupation of user') 
    parser.add_argument('--verbose', '-v', action='count', default=0) 
    args = parser.parse_args() 
    return args 

def main(args): 
    name = args.name 
    age = args.age 
    occupation = args.occupation 
    print(f"\nHello {name}.") 
    print(f"Your age is {age}. Therefore, you were probably born around {(dt.datetime.today() - dt.timedelta(days=age*365)).year}.") 
    print(f"Occupation is {occupation}.\n") 
    print(args)  
    if args.verbose == 1:
       print(f"\nMore info on {name}.")
    elif args.verbose == 2:
       print(f"\nEven more info on {name}.")
    elif args.verbose == 3:
       print(f"\nToo much information on {name}.")  
    elif args.verbose > 3:
       print(f"I will have to kill you for anymore info")
if __name__ == "__main__": 
    args = cli() 
    main(args)
