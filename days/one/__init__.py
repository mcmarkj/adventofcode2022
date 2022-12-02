from utils.common import filetostringlist, is_testing


def split_to_elves(input_content: list) -> list[list]:
    elves_pockets = []
    tmp = []
    for food_item in input_content:
        if food_item != "":
            tmp.append(int(food_item))
        else:
            elves_pockets.append(tmp)
            tmp = []
    elves_pockets.append(tmp)
    return elves_pockets


def sort_by_heaviest(elves_input: list[list]) -> list[list]:
    return sorted(elves_input, key=sum, reverse=True)


def part_one(input_content: list) -> str:
    elves = split_to_elves(input_content)
    heaviest_elf = sum(sort_by_heaviest(elves)[0])
    return heaviest_elf


def part_two(input_content: list) -> str:
    elves = split_to_elves(input_content)
    heaviest_elf = sum(sort_by_heaviest(elves)[0]) + sum(sort_by_heaviest(elves)[1]) + sum(sort_by_heaviest(elves)[2])
    return heaviest_elf


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/one/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
