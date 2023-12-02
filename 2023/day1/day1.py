import re
from word2number import w2n

total = 0

matches = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in open('input.txt'):
    #numbers = re.findall(r'\d', line)
    numbers = re.findall(r"(?=("+'|'.join(matches)+r"))", line)

    num1 = w2n.word_to_num(numbers[0])
    num2 = w2n.word_to_num(numbers[-1])
    line_number = f"{num1}{num2}"

    total += int(line_number)

print(total)
