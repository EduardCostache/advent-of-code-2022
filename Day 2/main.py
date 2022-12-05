filename = 'advent-of-code-2022\Day 2\input.txt'

shapeToPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

shapeDict = {
    #[lose, win, draw]
    'A': ['Z', 'Y', 'X'],
    'B': ['X', 'Z', 'Y'],
    'C': ['Y', 'X', 'Z']
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


def part2(lines):
    totalScore = 0

    for line in lines:
        currentScore = 0
        enemySign = line[0]
        roundType = line[2]

        # Z : win
        # X : lose
        # Y : draaw

        if roundType == 'Z':
            mySign = shapeDict[enemySign][1]

            currentScore += shapeToPoints[mySign] + 6
        elif roundType == 'Y':
            mySign = shapeDict[enemySign][2]

            currentScore += shapeToPoints[mySign] + 3
        else:
            mySign = shapeDict[enemySign][0]

            currentScore += shapeToPoints[mySign]

        totalScore += currentScore

    print(totalScore)


# part1(lines)
part2(lines)
