import time
from math import sqrt

FILENAME = "Day 9\input.txt"
TEST_FILE = "Day 9\\test.txt"

def openFile(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines

moves = openFile(FILENAME)

tailVisitedCoordinates = {
    (0,0)
}


def calculateDistance(hPos, tPos):
    diffX = hPos[0] - tPos[0]
    diffY = hPos[1] - tPos[1]

    sqrs = (diffX**2) + (diffY**2)

    return sqrt(sqrs) >= 2.0

def part1():
    hPos = [0,0] #x, y
    tPos = [0,0] #x, y

    prevHPos = [0,0] #x, y

    for move in moves:
        move = move.split(' ')
        direction = move[0]
        distance = int(move[1])

        if direction == 'R':
            for _ in range(distance):
                prevHPos = hPos.copy()
                hPos[0] += 1
                if calculateDistance(hPos, tPos):
                    tPos = prevHPos.copy()
                    tailVisitedCoordinates.add((tPos[0], tPos[1]))
                    

        elif direction == 'L':
            for _ in range(distance):
                prevHPos = hPos.copy()
                hPos[0] -= 1
                if calculateDistance(hPos, tPos):
                    tPos = prevHPos.copy()
                    tailVisitedCoordinates.add((tPos[0], tPos[1]))
                    

        elif direction == 'U':
            for _ in range(distance):
                prevHPos = hPos.copy()
                hPos[1] += 1
                if calculateDistance(hPos, tPos):
                    tPos = prevHPos.copy()
                    tailVisitedCoordinates.add((tPos[0], tPos[1]))
                    

        else: #move down
            for _ in range(distance):
                prevHPos = hPos.copy()
                hPos[1] -= 1
                if calculateDistance(hPos, tPos):
                    tPos = prevHPos.copy()
                    tailVisitedCoordinates.add((tPos[0], tPos[1]))
                    

    return len(tailVisitedCoordinates)
        

def part2():
    pass

print(part1())