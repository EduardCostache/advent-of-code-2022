filename = 'advent-of-code-2022\Day 1\input.txt'


def openFile(filename):
    lines = ""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


lines = openFile(filename)


def part1(lines):
    maxCalories = 0
    currentCalories = 0
    for line in lines:
        if line == '\n':
            currentCalories = 0
        else:
            currentCalories += int(line.strip())
            if currentCalories > maxCalories:
                maxCalories = currentCalories

    print(maxCalories)


def part2(lines):
    list = []
    totalCals = 0

    for line in lines:
        if line == '\n':
            list.append(totalCals)
            totalCals = 0
        else:
            totalCals += int(line.strip())

    list.sort()
    print(list[-1] + list[-2] + list[-3])


part2(lines)
