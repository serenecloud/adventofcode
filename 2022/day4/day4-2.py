overlapping = 0

for line in open("input.txt"):
    sections = line.split(",")
    first = sections[0].split("-")
    second = sections[1].split("-")

    elf1 = set(range(int(first[0]), int(first[1]) + 1))
    elf2 = set(range(int(second[0]), int(second[1]) + 1))

    for seat in elf1:
        if seat in elf2:
            overlapping += 1
            break

print(overlapping)
