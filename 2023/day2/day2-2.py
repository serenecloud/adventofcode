import re

def parse_line(line):
    parts = re.split(': |;', line)

    game = parts.pop(0).split(' ')

    game_id = int(game[1])

    print(game)

    min_red = 0
    min_blue = 0
    min_green = 0

    for handful in parts:
        reveal = handful.split(',')

        for single_colour in reveal:
            cubes = single_colour.strip().split(' ')
            number = int(cubes[0])
            colour = cubes[1]
            #print(number, colour)
            match colour:
                case 'red':
                    if number > min_red:
                        min_red = number
                case 'green':
                    if number > min_green:
                        min_green = number
                case 'blue':
                    if number > min_blue:
                        min_blue = number

    return min_red * min_green * min_blue

game_cube_sum = 0

for line in open('input.txt'):
    game_cube_sum += parse_line(line)
    print(game_cube_sum)
