from utils.common import filetostringlist, is_testing


def split_list(input_content: list) -> list[list[str]]:
    return [x.split(",") for x in input_content]


def lower_upper(input_content: list) -> list:
    lower_upper = []
    for x in input_content:
        lower_upper.append([y.split("-") for y in x])
    return lower_upper


def expand_indexes(input_content: list) -> list:
    expanded = []
    for x in input_content:
        pair1 = list(range(int(x[0][0]), int(x[0][1]) + 1))
        pair2 = list(range(int(x[1][0]), int(x[1][1]) + 1))
        expanded.append([pair1, pair2])
    return expanded


def check_lists(input_content: list) -> int:
    total = 0
    for pairs in input_content:
        if all(elem in pairs[0] for elem in pairs[1]) or all(elem in pairs[1] for elem in pairs[0]):
            total += 1
    return total


def check_matches(input_content: list) -> int:
    total = 0
    for pairs in input_content:
        if set(pairs[0]).intersection(set(pairs[1])):
            total += 1
    return total


def part_one(input_content: list) -> int:
    split = split_list(input_content)
    low_up = lower_upper(split)
    expanded = expand_indexes(low_up)
    total = check_lists(expanded)
    return total


def part_two(input_content: list) -> int:
    split = split_list(input_content)
    low_up = lower_upper(split)
    expanded = expand_indexes(low_up)
    total = check_matches(expanded)
    return total


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/four/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
