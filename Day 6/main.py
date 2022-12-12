import time
import math

filename = 'advent-of-code-2022\Day 6\input.txt'


def openFile(filename):
    f = open(filename, 'r')
    line = f.readline()
    f.close()
    return line


line = openFile(filename)


def checkWindow(start, end):
    i = start + 1

    window = []

    window.append(line[start])

    while i <= end:
        window.append(line[i])
        for j in reversed((range(len(window)-1))):
            if line[i] == window[j]:
                return False

        i += 1

    return True


def part1(line):
    i = 0
    j = i + 3
    length = len(line)

    while j < length:
        if checkWindow(i, j):
            return j+1
        i += 1
        j += 1


def part2(line):
    i = 0
    j = i + 13
    length = len(line)

    while j < length:
        if checkWindow(i, j):
            return j+1
        i += 1
        j += 1


timeStart = time.time()
print(part2(line))
print(f"Runtime: {round((time.time() - timeStart) * 1000, 1)}ms")
