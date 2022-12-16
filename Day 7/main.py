import time

FILENAME = 'advent-of-code-2022\Day 7\input.txt'
TEST_FILE = 'advent-of-code-2022\Day 7\\test.txt'
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
                if line[2] != "..":
                    currentDirectory.append(line[2])

                else:
                    currentDirectory.pop()

            else:
                continue
        elif line[0] == "dir":
            if line[1] not in allDirectories.keys():
                allDirectories.update({line[1]: 0})
            else:
                continue
        else:
            size = int(line[0])

            for directory in currentDirectory:
                allDirectories[directory] += size

    # print(allDirectories)

    for directory in allDirectories:

        size = allDirectories[directory]
        # print(size)
        if size <= 100000:
            totalSum += size
            print(f"{directory} : {size}")

    print(totalSum)


def part2():
    pass


part1()
