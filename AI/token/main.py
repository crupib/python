

# Press the green button in the gutter to run the script.
import re
def main():
    text = "Hello, world. This, is a test."
    result = re.split(r'(\s)', text)
    print("First Result")
    print(result)
    result = re.split(r'([,.]|\s)', text)
    print("2nd Result")
    print(result)
    print("Strip result")
    result = [item for item in result if item.strip()]
    print(result)
    print("3rd Result")
    print(result)
    # New text stuff
    print("New Text stuff")
    text1 = "Hello, world. Is this-- a test?"
    result = re.split(r'([,.:;?_!"()\']|--|\s)', text1)
    result = [item.strip() for item in result if item.strip()]
    print(result)
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
