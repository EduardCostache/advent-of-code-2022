import time

FILENAME = 'Day 7\input.txt'
TEST_FILE = 'Day 7\\test.txt'
currentDirectory = []
allDirectories = {
    '/': 0
}


def openFile(file):
    commands = []
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        commands.append(line.strip())

    f.close()
    return commands


commands = openFile(FILENAME)


def part1():
    totalSum = 0

    for line in commands:
        line = line.split(' ')

        if line[0] == '$':
            if line[1] == "cd":
                if line[2] == "..":
                    currentDirectory.pop()
                else:
                    currentDirectory.append(line[2])
                    allDirectories.update({"_".join(currentDirectory) : 0})
            else:
                continue # if the command is 'ls' we ignore it and move on
        elif line[0] == "dir":
            continue
        else:
            size = int(line[0])
            for i in range(0, len(currentDirectory)):
                directory = "_".join(currentDirectory[0:i+1])
                allDirectories[directory] += size

    for directory in allDirectories:
        size = allDirectories[directory]
        if size <= 100_000:
            totalSum += size

    print(f"Part 1: {totalSum}")


def part2():
    part1()

    totalUsedSpace = allDirectories['/']
    totalUnUsedSpace = 70_000_000 - totalUsedSpace
    requiredSpace = 30_000_000 - totalUnUsedSpace 

    sortedSizes = []

    for size in allDirectories.values():
        if size >= requiredSpace:
            sortedSizes.append(size)

    sortedSizes.sort()

    print(f"Part 2: {sortedSizes[0]}")

timeStart = time.time()
part2()
print(f"Runtime: {round((time.time() - timeStart) * 1000, 1)}ms")
