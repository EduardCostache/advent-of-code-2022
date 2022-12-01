#----------------------------------- PART 1 -----------------------------------#
maxCalories = 0
currentCalories = 0
lines = ""


with open('advent-of-code-2022\Day 1\input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    if line == '\n':
        currentCalories = 0
    else:
        currentCalories += int(line.strip())
        if currentCalories > maxCalories:
            maxCalories = currentCalories

print(maxCalories)
