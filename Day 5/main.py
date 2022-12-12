import time

FILENAME = 'advent-of-code-2022\Day 5\input.txt'


def openFile(filename):
    crates = []
    inputs = []
    f = open(filename, 'r')

    line = f.readline()

    while line:
        crates.append(line.replace('\n', ''))
        line = f.readline()

        if not line or line == '\n':
            break

    line = f.readline()

    while line:
        inputs.append(line.replace('\n', ''))
        line = f.readline()

        if not line:
            break

    f.close()

    numberOfStacks = crates.pop(len(crates)-1).strip()[-1]
    return crates, inputs, int(numberOfStacks)


crates, inputs, numberOfStacks = openFile(FILENAME)


def formatCrates(crates, nStacks):
    allStacks = []
    for _ in range(nStacks):
        allStacks.append([])

    lineLength = len(crates[1])
    for line in crates:
        count = 0
        for c in range(1, lineLength, 4):
            if line[c] != ' ':
                allStacks[count].append(line[c])
            count += 1

    for stack in allStacks:
        stack = stack.reverse()

    return allStacks


crates = formatCrates(crates, numberOfStacks)


def readInput(line):
    line = line.split(' ')

    nMoves = int(line[1])
    # Subtract 1 for index
    moveFrom = int(line[3]) - 1
    moveTo = int(line[-1]) - 1

    return nMoves, moveFrom, moveTo


def getTopCrates(crates):
    result = []

    for stack in crates:
        if len(stack) == 0:
            continue
        result.append(stack[-1])

    return "".join(result)


def part1(crates,  inputs):
    for line in inputs:

        nMoves, moveFrom, moveTo = readInput(line)

        for _ in range(nMoves):
            temp = crates[moveFrom].pop()
            crates[moveTo].append(temp)

    print(getTopCrates(crates))


def part2(crates, inputs):
    for line in inputs:

        nMoves, moveFrom, moveTo = readInput(line)

        temp = []
        for _ in range(nMoves):
            temp.append(crates[moveFrom].pop())

        temp.reverse()

        for crate in temp:
            crates[moveTo].append(crate)

    print(getTopCrates(crates))


timeStart = time.time()
#part1(crates, inputs)
#part2(crates, inputs)
print(f"Runtime: {time.time() - timeStart}s")
