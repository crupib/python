counts = []


def printInstructions(instruction):
    print(instruction)


def getUserScore(userName):
    filename = open("userScores.txt", "r")
    for line in filename:
        counts.append(line.split(","))
    for ustring in counts:
        if userName == ustring[0]:
            print("user in counts")


userName = ""
getUserScore("Darren")
print(counts)
