begin = False
rows_done = False

offset = 4
# columns = [1, 5, 9, 13, 17, 21, 25, 29, 33]
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

stacks = {}

for line in reversed(open("input.txt").readlines()):
    if line == "\n":
        begin = True

    line = line.replace("\n", "")

    if begin and line:
        show = ""
        for column in columns:
            char_offset = (column - 1) * offset + 1
            if line[1] == "1":
                stacks[column] = []
            else:
                if line[char_offset] != " ":
                    stacks[column].append(line[char_offset])

        rows_done = True


for key in stacks.keys():
    print(key, stacks[key])

for line in open("input.txt"):
    if line[0:4] == "move":
        print(line)
        instructions = line.split(" ")
        count = int(instructions[1])
        source = int(instructions[3])
        destination = int(instructions[5])

        moving_stack = stacks[source][-count:]
        # stacks[destination].append(moving_stack)
        for item in moving_stack:
            stacks[destination].append(item)
        del stacks[source][-count:]

        for key in stacks.keys():
            print(key, stacks[key])


print("=========== res =============")
for key in stacks.keys():
    print(key, stacks[key])
