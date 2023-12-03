from utils.read import read_file


def part_one(_input):
    expected_red = 12
    expected_green = 13
    expected_blue = 14
    sum_game_ids = 0

    for line in _input:
        line = line.replace("Game ", "")
        game_number = int(line.split(":")[0])
        pulls = line.split(":")[1].split(";")
        possible_game = True
        for pull in pulls:
            pull = pull.lstrip()
            colors = pull.split(",")
            for color in colors:
                color = color.lstrip().rstrip()
                if "red" in color:
                    color_number = int(color.replace("red", ""))
                    if color_number > expected_red:
                        possible_game = False
                        break
                if "blue" in color:
                    color_number = int(color.replace("blue", ""))
                    if color_number > expected_blue:
                        possible_game = False
                        break
                if "green" in color:
                    color_number = int(color.replace("green", ""))
                    if color_number > expected_green:
                        possible_game = False
                        break
        if possible_game:
            sum_game_ids += game_number
    print(f"The sum of all impossible game Ids is: {sum_game_ids}")


def part_two(_input):
    power_of_games = 0
    for line in _input:
        red = 0
        blue = 0
        green = 0
        line = line.replace("Game ", "")
        pulls = line.split(":")[1].split(";")
        for pull in pulls:
            pull = pull.lstrip()
            colors = pull.split(",")
            for color in colors:
                color = color.lstrip().rstrip()
                if "red" in color:
                    color_number = int(color.replace("red", ""))
                    if color_number > red:
                        red = color_number
                if "blue" in color:
                    color_number = int(color.replace("blue", ""))
                    if color_number > blue:
                        blue = color_number
                if "green" in color:
                    color_number = int(color.replace("green", ""))
                    if color_number > green:
                        green = color_number
        power_of_game = red * blue * green
        power_of_games += power_of_game
    print(f"The sum of the power of all games is: {power_of_games}")


if __name__ == "__main__":
    stringInput = read_file(2, "string", False)
    part_one(stringInput)
    part_two(stringInput)
