from utils.read import read_file

def make_number_list(_input):
    split = _input.strip().split(" ")
    while "" in split:
        split.remove("")
    return [int(s) for s in split]

def part_one(_input):
    all_points = 0
    for line in _input:
        line = line.replace("Card ", "")
        card_number = int(line.split(":")[0])
        card = line.split(":")[1]
        winning_numbers = make_number_list(card.split("|")[0])
        owned_numbers = make_number_list(card.split("|")[1])
        matches = set(winning_numbers) & set(owned_numbers)
        points = 0
        if len(matches) >= 1:
            points = 1
        for i in range(1, len(matches)):
            points = points * 2
        all_points += points
    print(f"All scratchcards combined are worth {all_points} points")


def part_two(_input):
    pass

if __name__ == "__main__":
    stringInput = read_file(4, "string", False)
    part_one(stringInput)
    part_two(stringInput)
