import os
counts = []


def printInstructions(instruction):
    print(instruction)


def updateUserScore(newUser, userName, score):
    if newUser == True:
        try:
            filename = open("userScores.txt", "a")
            filename.write("%s, %s\n" % (userName, score))
            filename.close()
            return(0)
        except IOError:
            print("no userScores.txt file")
            filename = open("userScores.txt", "w")
            filename.write(userName, score)
            filename.close()
            return(0)

    else:
        tmpname = open("userScores.tmp", "w")
        filename = open("userScores.txt", "r")
        for line in filename:
            counts.append(line.split(","))
        for name_score in counts:
            if userName == name_score[0]:
                tmpname.write("%s, %s\n" % (userName, score))
            else:
                tmpname.write("%s, %s" % (name_score[0], name_score[1]))
        tmpname.close()
        filename.close()
        os.rename("userScores.txt","_userScores.txt")
        os.rename("userScores.tmp","userScores.txt")


def getUserScore(userName):
    try:
        filename = open("userScores.txt", "r")
    except IOError:
        filename = open("userScores.txt", "w")
        filename.close()
        return (-1)
    for line in filename:
        counts.append(line.split(","))
    for name_score in counts:
        if userName == name_score[0]:
            filename.close()
            return(name_score[1])
        else:
            continue
    filename.close()
    return(-1)


# Main  #
userName = ""
#score = getUserScore("Benny")
# print(score)
updateU = updateUserScore(False, "Darren", "299")
#print('update user {0} \n'.format(updateU))
