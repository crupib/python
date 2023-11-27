import math
def check_user_input(input) -> str:
    try:
        # Convert it into integer
        val = int(input)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
        except ValueError:
            return "NAN"
def convert_radians_degrees(rad: float) -> float:
     return math.degrees(rad)

def formula_convert_radians_degrees(rad: float) -> float:
     return 180/(math.pi*rad) 

input1 = input("Enter radians ")
error_check=check_user_input(input1)
if error_check == "NAN":
   print("Try again it has to be a number\n")
   exit()
print(convert_radians_degrees(float(input1)))
print(formula_convert_radians_degrees(float(input1)))
