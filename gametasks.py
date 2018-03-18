counts = []


def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    filename = open("userScores.txt", "r")
    for line in filename:
        counts.append(line.split(","))
    for name_score in counts:
        if userName == name_score[0]:
            return(name_score[1])
        else:
            continue
    return(-1)
# Main  #
userName = ""
score = getUserScore("xenny")
print(score)
