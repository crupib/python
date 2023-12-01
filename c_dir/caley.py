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

    if(choice == '2'):  # Lookup the password
        passwords = loadPasswordFile(passwordFileName)
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input()
        for keyvalue in passwords:
            if(keyvalue[0] == passwordToLookup):
                unencrypt = passwordDcrypt(keyvalue[1], 16)
                print(keyvalue[0] + ' ' + unencrypt)

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()
        encrypted_password = passwordEncrypt(unencryptedPassword, 16)
        testlist = [website, encrypted_password]
        passwords.append(testlist)
        savePasswordFile(passwords, passwordFileName)

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
