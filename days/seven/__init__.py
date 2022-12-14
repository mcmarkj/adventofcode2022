from utils.common import filetostringlist, is_testing


def is_command(input_str: str) -> bool:
    if input_str.startswith("$"):
        return True
    return False


def command_type(input_str: str) -> [str]:
    if input_str.startswith("$ cd"):
        return "CD"
    else:
        return "LS"


def get_type(input_str: str) -> str:
    if input_str.startswith("dir"):
        return "DIR"
    return "FILE"


def split_files(input_str: str) -> [int, str]:
    return input_str.split()[0], input_str.split()[1]


def get_directory_size(input_content: list) -> dict:
    directories = {"/": 0}
    current_dir = []
    current_dir_size = 0
    for line in input_content:
        dir_name = "/".join(current_dir).replace("//", "/")
        if is_command(line) and command_type(line) == "CD":
            current_dir_size = 0
            new_dir = line.split()[2]
            if new_dir == "..":
                current_dir.pop()
            else:
                current_dir.append(new_dir)
        elif not is_command(line) and get_type(line) == "FILE":
            size, name = split_files(line)
            current_dir_size += int(size)
            directories[dir_name] = int(current_dir_size)
    return directories


def recrusive_tally(dir_structure: dir) -> dir:
    for dir in dir_structure:
        for dirs in dir_structure:
            if dirs != dir and str(dirs).startswith(str(dir)):
                dir_structure[dir] += dir_structure[dirs]
    return dir_structure


def part_one(input_content: list) -> int:
    structure = get_directory_size(input_content)
    structure = recrusive_tally(structure)
    print(structure)
    return sum(v for v in structure.values() if v <= 100000)


def part_two(input_content: list) -> int:
    return 0


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/seven/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
