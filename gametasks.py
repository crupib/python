def printInstructions(instruction):
    print(instruction)


def updateUserScore(newUser, userName, score):
    from os import remove, rename
    if newUser == True:
        input = open("userScores.txt", "a")
        input.write(userName + ', ' +  score + '\n')
        input.close()
    else:
        temp = open("userScores.tmp", "w")
        input = open("userScores.txt", "r")
        for line in input:
            content = (line.split(","))
            if content[0] == userName:
                input.write(userName + ', ' +  score + '\n')
            else:
                temp.write(line)
        temp.close()
        input.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")


def getUserScore(userName):
    try:
        input = open("userScores.txt", "r")
        for line in input:
            content = line.split(", ")
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        input = open('userScores.txt', 'w')
        input.close()
        return '-1'
