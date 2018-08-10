import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]
# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"
# The encryption key for the caesar cypher
encryptionKey = 16
# Caesar Cypher Encryption

def passwordEncrypt(unencryptedMessage, key):
    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''
    # For each symbol in the unencryptedMessage we will add an encrypted
    # symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage

# Caesar Cypher Decryption


def passwordDcrypt(message, key):
    # We will start with an empty string as our decryptedMessage
    key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


def loadPasswordFile(fileName):
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)
    return passwordList


def savePasswordFile(passwordList, fileName):
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-4)")
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if(choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()
        for keyvalue in passwords:
            if(keyvalue[0] == passwordToLookup):
                unencrypt = passwordDcrypt(keyvalue[1], 16)
                print(keyvalue[0] + ' ' + unencrypt)

        ####### YOUR CODE HERE ######
        # You will need to find the password that matches the website
        # You will then need to decrypt the password
        #
        # 1. Create a loop that goes through each item in the password list
        #  You can consult the reading on lists in Week 5 for ways to loop through a list
        #
        # 2. Check if the name is found.  To index a list of lists you use 2 square backet sets
        #   So passwords[0][1] would mean for the first item in the list get it's 2nd item (remember, lists start at 0)
        #   So this would be 'XqffoZeo' in the password list given what is predefined at the top of the page.
        #   If you created a loop using the syntax described in step 1, then i is your 'iterator' in the list so you
        #   will want to use i in your first set of brackets.
        #
        # 3. If the name is found then decrypt it.  Decrypting is that exact reverse operation from encrypting.  Take a look at the
        # caesar cypher lecture as a reference.  You do not need to write your own decryption function, you can reuse passwordEncrypt
        #
        #  Write the above one step at a time.  By this I mean, write step 1...  but in your loop print out every item in the list
        #  for testing purposes.  Then write step 2, and print out the password but not decrypted.  Then write step 3.  This way
        #  you can test easily along the way.
        #
        ####### YOUR CODE HERE ######
    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()
        encrypted_password = passwordEncrypt(unencryptedPassword, 16)
        testlist = [website, encrypted_password]
        passwords.append(testlist)

        ####### YOUR CODE HERE ######
        # You will need to encrypt the password and store it in the list of passwords
        # The encryption function is already written for you
        # Step 1: You can say encryptedPassword = passwordEncrypt(unencryptedPassword,encryptionKey)]
        # the encryptionKey variable is defined already as 16, don't change this
        # Step 2: create a list of size 2, first item the website name and the second item the password.
        # Step 3: append the list from Step 2 to the password list

        ####### YOUR CODE HERE ######

    if(choice == '4'):  # Save the passwords to a file
        savePasswordFile(passwords, passwordFileName)
    if(choice == '5'):  # print out the password list
        passwords = loadPasswordFile(passwordFileName)
        for id,keyvalue in passwords:
            unencrypt = passwordDcrypt(keyvalue, 16) 
            print(id, unencrypt)
    if(choice == '6'):  # quit our program
        sys.exit()

    print()
    print()
