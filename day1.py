import re
from utils.read import read_file

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def part_one(_input):
    numberList = []
    for line in _input:
        numberListFromString = re.findall(r'\d+', line)
        numberString = ''.join(numberListFromString)
        first = numberString[0]
        last = numberString[-1]
        numberList.append(int(f"{first}{last}"))
    print(f"The sum of all calibration values is: {sum(numberList)}")


def part_two(_input):
    for i in range(1, 10):
        number_dict[str(i)] = i

    _sum = 0
    for line in _input:
        first = None
        first_index = len(line) + 1
        last = None
        last_index = -1

        for key, value in number_dict.items():
            if key not in line:
                continue

            x = line.index(key)
            y = line.rindex(key)

            if x < first_index:
                first = value
                first_index = x

            if y > last_index:
                last = value
                last_index = y

        if first is not None and last is not None:
            _sum += int(str(first) + str(last))
    print(f"The sum of all calibration values is: {_sum}")


if __name__ == "__main__":
    stringInput = read_file(1, "string", False)
    part_one(stringInput)
    part_two(stringInput)
