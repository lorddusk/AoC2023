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
    numberList = []
    for line in _input:
        original_line = line
        for item in number_dict:
            line = line.replace(item, str(number_dict[item]))
        numberListFromString = re.findall(r'\d+', line)
        numberString = ''.join(numberListFromString)
        first = numberString[0]
        last = numberString[-1]

        digit = int(f"{first}{last}")
        print(f"{original_line}: {line}: {digit}")
        numberList.append(digit)
    if sum(numberList) > 53652:
        print(f"The sum of all calibration values is: {sum(numberList)}")
    else:
        print(f"too low: {sum(numberList)}")

if __name__ == "__main__":
    stringInput = read_file(1, "string", True)
    # part_one(stringInput)
    part_two(stringInput)

