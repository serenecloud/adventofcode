import re

total = 0

for line in open('input.txt'):
    numbers = re.findall(r'\d', line)
    line_number = f"{numbers[0]}{numbers[-1]}"

    total += int(line_number)

print(total)
