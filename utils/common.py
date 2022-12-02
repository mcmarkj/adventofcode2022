import os
from typing import List
from pandas import DataFrame


def filetostringlist(filename: str) -> List[str]:
    with open(filename) as f:
        input = [line.rstrip() for line in f]
        return input


def filetointlist(filename: str) -> List[int]:
    with open(filename) as f:
        input = [int(line.rstrip()) for line in f]
        return input


def filetodpdataframe(filename: str) -> DataFrame:
    data = filetointlist(filename)
    df = DataFrame(data)
    return df


def get_file(file_name: str) -> list:
    with open(file_name, "r") as input_file:
        print(input_file.readlines())
        print("")
        lines = input_file.readlines()
    return lines


def is_testing() -> bool:
    return str_to_bool(os.getenv("TEST"))


def str_to_bool(bool_str: str) -> bool:
    if bool_str.lower() == "true":
        return True
    elif bool_str.lower() == "false":
        return False
    else:
        raise ValueError(f"{bool_str} isn't a bool option")
