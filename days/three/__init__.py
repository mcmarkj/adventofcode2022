from utils.common import filetostringlist, is_testing


def get_subtraction(input: str) -> int:
    if input.isupper():
        return -38
    else:
        return -96


def get_priority(input: str) -> int:
    return ord(input) + get_subtraction(input)


def split_compartments(input: str) -> list[str]:
    half, rem = divmod(len(input), 2)
    return [input[: half + rem], input[half + rem :]]


def get_groups(input_content: list) -> list[list[str]]:
    groups = []
    start = 0
    end = len(input_content)
    step = 3
    for i in range(start, end, step):
        x = i
        groups.append(input_content[x : x + step])
    return groups


def find_common_item(input: list[str]) -> str:
    try:
        return list(set(input[0]).intersection(input[1], input[2]))[0]
    except:
        return list(set(input[0]).intersection(input[1]))[0]


def part_one(input_content: list) -> str:
    split = [split_compartments(s) for s in input_content]
    commons = [find_common_item(s) for s in split]
    priorities = [get_priority(s) for s in commons]
    return sum(priorities)


def part_two(input_content: list) -> str:
    split = get_groups(input_content)
    commons = [find_common_item(s) for s in split]
    priorities = [get_priority(s) for s in commons]
    return sum(priorities)


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/three/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
