filename = 'advent-of-code-2022\Day 4\input.txt'


def openFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


lines = openFile(filename)


def splitRanges(line):
    line = line.strip()

    splitLine = line.split(',')

    x1, x2 = splitLine[0].split('-')
    y1, y2 = splitLine[1].split('-')

    return int(x1), int(x2), int(y1), int(y2)


def doesContain(x1, x2, y1, y2):
    xLen = (x2 - x1) + 1
    yLen = (y2 - y1) + 1

    if xLen > yLen:
        if x2 >= y2 and x1 <= y1:
            return True
    elif xLen < yLen:
        if y1 <= x1 and y2 >= x2:
            return True
    else:
        if x1 == y1 and x2 == y2:
            return True

    return False


def part1(lines):
    total = 0
    for line in lines:
        x1, x2, y1, y2 = splitRanges(line)
        result = doesContain(x1, x2, y1, y2)

        if result:
            total += 1

    return total


def doesOverlap(x1, x2, y1, y2):
    setX = set(range(x1, x2+1))
    setY = set(range(y1, y2+1))

    if len(setX.intersection(setY)) > 0:
        return True

    return False


def part2(lines):
    total = 0
    for line in lines:
        x1, x2, y1, y2 = splitRanges(line)

        if doesOverlap(x1, x2, y1, y2):
            total += 1

    return total


# print(part1(lines))
print(part2(lines))
