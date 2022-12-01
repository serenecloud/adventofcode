elves = {}
count = 1

calories = 0
for line in open("input.txt"):
    if line == "\n":
        elves[count] = calories
        calories = 0
        count += 1
    else:
        calories += int(line)

print(dict(sorted(elves.items(), key=lambda item: item[1], reverse=True)[0:3]))
