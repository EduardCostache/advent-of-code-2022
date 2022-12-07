import string

filename = 'advent-of-code-2022\Day 3\input.txt'
alphabet = list(string.ascii_letters)


def openFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


lines = openFile(filename)


def part1(lines):
    total = 0
    charOccurances = [0] * 58
    OFFSET = 65

    for line in lines:
        commonChar = ''
        halfLength = int(len(line)/2)

        firstComp = line[0:halfLength]
        secondComp = line[halfLength:]

        for c in firstComp:
            index = ord(c) - OFFSET
            charOccurances[index] += 1

        for c in secondComp:
            index = ord(c) - OFFSET

            if charOccurances[index] == 0:
                continue
            else:
                commonChar = c
                break

        total += alphabet.index(commonChar) + 1

        charOccurances = [0] * 58

    print(total)


def part2(lines):
    total = 0
    OFFSET = 65
    newLines = []

    # Grouping the lines
    for i in range(0, len(lines), 3):
        newLines.append(lines[i:i+3])

    for group in newLines:
        charOccurances1 = set()
        charOccurances2 = set()
        charOccurances3 = set()

        for count, line in enumerate(group):
            line = line.replace('\n', '')
            if count == 0:
                for c in line:
                    charOccurances1.add(c)
            elif count == 1:
                for c in line:
                    charOccurances2.add(c)
            else:
                for c in line:
                    charOccurances3.add(c)

            charOccurances3 = charOccurances3.intersection(
                charOccurances1, charOccurances2)

            for x in charOccurances3:
                total += alphabet.index(x) + 1

    print(total)


# part1(lines)
part2(lines)
