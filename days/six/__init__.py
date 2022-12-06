from utils.common import filetostringlist, is_testing


def split_chars(input_content: list) -> list:
    return [*input_content[0]]


def find_start_marker(input_content: list, marker_point: int = 4) -> int:
    chars = []
    for c in range(len(input_content)):
        character = input_content[c]
        if len(chars) == marker_point:
            chars.remove(chars[0])
        chars.append(character)
        if is_valid_marker(chars, marker_point):
            return c + 1


def is_valid_marker(packets: list, marker_point: int = 4) -> bool:
    return True if (len(set(packets))) == marker_point else False


def part_one(input_content: list) -> int:
    return find_start_marker(input_content)


def part_two(input_content: list) -> int:
    return find_start_marker(input_content, 14)


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/six/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    input_content = split_chars(input_content)
    print(part_one(input_content))
    print(part_two(input_content))
