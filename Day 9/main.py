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

def calculateDistance(hx, hy, tx, ty):
    diffX = tx - hx
    diffY = ty - hy

    sqrs = (diffX**2) + (diffY**2)

    return sqrt(sqrs)

def updateCoords(hx, hy, tx, ty, prevHX, prevHY):
    pass

def part1():
    hx, hy = 0,0
    tx, ty = 0,0

    prevHX, prevHY = 0,0



    for move in moves:
        direction = move[0]
        speed = int(move[2])

        prevHX, prevHY = hx, hy

        if direction == 'R':
            for _ in range(speed):
                prevHX, prevHY = hx, hy
                hx += 1
                if calculateDistance(hx, hy, tx, ty) >= 2.0:
                    tx, ty = prevHX, prevHY
                    tailVisitedCoordinates.add((tx, ty))
                print(f"Head: {hx},{hy}   Tail: {tx},{ty}")
        elif direction == 'L':
            for _ in range(speed):
                prevHX, prevHY = hx, hy
                hx -= 1
                if calculateDistance(hx, hy, tx, ty) >= 2.0:
                    tx, ty = prevHX, prevHY
                    tailVisitedCoordinates.add((tx, ty))
                print(f"Head: {hx},{hy}   Tail: {tx},{ty}")
        elif direction == 'U':
            for _ in range(speed):
                prevHX, prevHY = hx, hy
                hy += 1
                if calculateDistance(hx, hy, tx, ty) >= 2.0:
                    tx, ty = prevHX, prevHY
                    tailVisitedCoordinates.add((tx, ty))
                print(f"Head: {hx},{hy}   Tail: {tx},{ty}")
        elif direction == 'D':
            for _ in range(speed):
                prevHX, prevHY = hx, hy
                hy -= 1
                if calculateDistance(hx, hy, tx, ty) >= 2.0:
                    tx, ty = prevHX, prevHY
                    tailVisitedCoordinates.add((tx, ty))
                print(f"Head: {hx},{hy}   Tail: {tx},{ty}")
        
    print(len(tailVisitedCoordinates))
        

def part2():
    pass

part1()