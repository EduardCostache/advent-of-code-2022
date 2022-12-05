filename = 'advent-of-code-2022\Day 2\input.txt'

shapeToPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# A | X = Rock
# B | Y = Paper
# C | Z = Scissor


def openFile(filename):
    lines = ""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


lines = openFile(filename)


def part1(lines):
    totalScore = 0
    for line in lines:
        currentScore = 0
        enemySign = line[0]
        mySign = line[2]
        if enemySign == 'A':
            if mySign == 'X':
                currentScore += 3
            elif mySign == 'Y':
                currentScore += 6

        if enemySign == 'B':
            if mySign == 'Y':
                currentScore += 3
            elif mySign == 'Z':
                currentScore += 6

        if enemySign == 'C':
            if mySign == 'Z':
                currentScore += 3
            elif mySign == 'X':
                currentScore += 6

        totalScore += currentScore + shapeToPoints[line[2]]

    print(totalScore)


def part2():
    pass


part1(lines)
