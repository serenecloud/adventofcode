import re

red_max = 12
green_max = 13
blue_max = 14


def parse_line(line):
    parts = re.split(': |;', line)

    game = parts.pop(0).split(' ')

    game_id = int(game[1])

    print(game)

    for handful in parts:
        reveal = handful.split(',')

        for single_colour in reveal:
            cubes = single_colour.strip().split(' ')
            number = int(cubes[0])
            colour = cubes[1]
            #print(number, colour)
            match colour:
                case 'red':
                    if number > red_max:
                        return 0
                case 'green':
                    if number > green_max:
                        return 0
                case 'blue':
                    if number > blue_max:
                        return 0

    print("Possible")
    return game_id

game_id_sum = 0

for line in open('input.txt'):
    game_id_sum += parse_line(line)
    print(game_id_sum)
