from utils.common import filetostringlist, is_testing


def part_one(input_content: list) -> int:
    return 0


def part_two(input_content: list) -> int:
    return 0


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/six/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
