import time

FILENAME = "Day 8\input.txt"
TEST_FILE = "Day 8\\test.txt"

def openFile(file):
    grid = []
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        grid.append(line)

    f.close()
    return grid

grid = openFile(FILENAME)

def isVisible(x, y, length):
    tree = int(grid[x][y])
    left, right, down, up = False, False, False, False
    # Check left
    for i in range(0,y):
        if int(grid[x][i]) >= tree:
            left = True

    # Check right
    for i in range(y+1, length):
        if int(grid[x][i]) >= tree:
            right = True

    # Check down
    for i in range(0, x):
        if int(grid[i][y]) >= tree:
            down = True

    # Check up
    for i in range(x+1, length):
        if int(grid[i][y]) >= tree:
            up = True
    
    return left & right & up & down

def getScore(x, y, length):
    tree = int(grid[x][y])
    scores = [0,0,0,0]

    # Check left
    for i in reversed(range(0,y)):
        scores[0] += 1
        if int(grid[x][i]) >= tree:
            break

    # Check right
    for i in range(y+1, length):
        scores[1] += 1
        if int(grid[x][i]) >= tree:
            break

    # Check down
    for i in range(x+1, length):
        scores[2] += 1
        if int(grid[i][y]) >= tree:
            break

    # Check up
    for i in reversed(range(0,x)):
        scores[3] += 1
        if int(grid[i][y]) >= tree:
            break

    return scores[0] * scores[1] * scores[2] * scores[3]

def part1():
    length = len(grid)
    totalVisibleTrees = (length*4) - 4 # Outer trees
    
    for x in range(1,length-1):
        for y in range(1, length-1):
            if grid[x][y] == 0:
                continue
            else:
                if not isVisible(x, y, length):
                    totalVisibleTrees += 1

    print(f"Part 1 : {totalVisibleTrees}")

def part2():
    length = len(grid)
    maxScenicScore = 0
    
    for x in range(1,length-1):
        for y in range(1, length-1):
            maxScenicScore = max(maxScenicScore, getScore(x, y, length))

    print(f"Part 2 : {maxScenicScore}")

timeStart = time.time()
part1()
print(f"Runtime: {round((time.time() - timeStart) * 1000, 1)}ms")
print()
timeStart = time.time()
part2()
print(f"Runtime: {round((time.time() - timeStart) * 1000, 1)}ms")