from utils.common import filetostringlist, is_testing
import string
import re


def build_blocks(input_stacks: str) -> list:
    block_list = []
    for i in range(9):
        block_list.append([])
    for line in reversed(input_stacks.splitlines()[:8]):
        j = -1
        for i in range(1, len(line), 4):
            j += 1
            if line[i] in set(string.ascii_uppercase):
                block_list[j].append(line[i])
    return block_list


def parse_moves(input_moves: list) -> list[int]:
    return [re.findall(r"move (\d{1,2}) from (\d{1,2}) to (\d{1,2})", move)[0] for move in input_moves]


def make_moves(block_list: list, moves: list, reversed_moves: bool = False) -> list:
    for move in moves:
        moves_to_make = int(move[0])
        move_from = int(move[1]) - 1
        move_to = int(move[2]) - 1
        on_crane = block_list[move_from][-moves_to_make:]
        block_list[move_from] = block_list[move_from][:-moves_to_make]
        if reversed_moves:
            block_list[move_to].extend(reversed(on_crane))
        else:
            block_list[move_to].extend(on_crane)
    return block_list


def on_top(block_list: list) -> str:
    end_str = ""
    for stack in block_list:
        end_str += str(stack[-1:][0])
    return end_str


def part_one(input_moves: list, input_stacks: str) -> str:
    blocks = build_blocks(input_stacks)
    moves = parse_moves(input_moves)
    moved_blocks = make_moves(blocks, moves)
    return on_top(moved_blocks)


def part_two(input_moves: list, input_stacks: list) -> int:
    blocks = build_blocks(input_stacks)
    moves = parse_moves(input_moves)
    moved_blocks = make_moves(blocks, moves, reversed_moves=True)
    return on_top(moved_blocks)


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/five/"
    input_file = "test_moves.txt" if test else "input_moves.txt"
    input_moves = filetostringlist(f"{directory}{input_file}")
    input_file = "test_stacks.txt" if test else "input_stacks.txt"
    input_stacks = open(f"{directory}{input_file}").read()
    print(part_one(input_moves, input_stacks))
    print(part_two(input_moves, input_stacks))
