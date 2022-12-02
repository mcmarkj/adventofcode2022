from utils.common import filetostringlist, is_testing

APPOINENT_OPTIONS = {"a": "rock", "b": "paper", "c": "scissors"}
ELF_OPTIONS = {"x": "rock", "y": "paper", "z": "scissors"}
SCORES = {"rock": 1, "paper": 2, "scissors": 3}
LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

ACTUAL_ELF_OPTIONS = {"x": "lose", "y": "draw", "z": "win"}
WINNERS = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
LOSERS = {"paper": "rock", "rock": "scissors", "scissors": "paper"}


def split_plays(input_content: list) -> list[str]:
    return [play.split() for play in input_content]


def translate_plays(input_content: list) -> list[list[str]]:
    plays = []
    for play in input_content:
        tmp = []
        tmp.append(APPOINENT_OPTIONS[play[0].lower()])
        tmp.append(ELF_OPTIONS[play[1].lower()])
        plays.append(tmp)
    return plays


def translate_act_to_score(act: str) -> int:
    return SCORES[act]


def play_rock(verses: str) -> bool:
    if verses == "paper":
        return False
    if verses == "scissors":
        return True


def play_paper(verses: str) -> bool:
    if verses == "rock":
        return True
    if verses == "scissors":
        return False


def play_scissors(verses: str) -> bool:
    if verses == "rock":
        return False
    if verses == "paper":
        return True


def determine_winner(player_one: str, player_two: str) -> int:
    if player_one == player_two:
        return 0
    if player_one == "scissors":
        if play_scissors(player_two):
            return 1
    elif player_two == "scissors":
        if play_scissors(player_one):
            return 2
    if player_one == "paper":
        if play_paper(player_two):
            return 1
    elif player_two == "paper":
        if play_paper(player_one):
            return 2
    if player_one == "rock":
        if play_rock(player_two):
            return 1
    elif player_two == "rock":
        if play_rock(player_one):
            return 2


def determine_score(input_content: list) -> int:
    points = 0
    for play in input_content:
        result = determine_winner(play[0], play[1])
        if result == 0:
            points += SCORES[play[1]] + DRAW_SCORE
        if result == 1:
            points += SCORES[play[1]] + LOSS_SCORE
        if result == 2:
            points += SCORES[play[1]] + WIN_SCORE
    return points


def get_desired_result(plays: list) -> list:
    new_plays = []
    for play in plays:
        tmp = []
        tmp.append(APPOINENT_OPTIONS[play[0].lower()])
        if ACTUAL_ELF_OPTIONS[play[1].lower()] == "win":
            tmp.append(WINNERS[APPOINENT_OPTIONS[play[0].lower()]])
        elif ACTUAL_ELF_OPTIONS[play[1].lower()] == "lose":
            tmp.append(LOSERS[APPOINENT_OPTIONS[play[0].lower()]])
        else:
            tmp.append(APPOINENT_OPTIONS[play[0].lower()])
        new_plays.append(tmp)
    return new_plays


def part_one(input_content: list) -> int:
    split = split_plays(input_content)
    plays = translate_plays(split)
    return determine_score(plays)


def part_two(input_content: list) -> int:
    split = split_plays(input_content)
    new_plays = get_desired_result(split)
    print(new_plays)
    return determine_score(new_plays)


def run(test: bool = None):
    if not test:
        test = is_testing()
    directory = "/Users/markmcwhirter/Documents/personal/adventofcode2022/days/two/"
    input_file = "test.txt" if test else "input.txt"
    input_content = filetostringlist(f"{directory}{input_file}")
    print(part_one(input_content))
    print(part_two(input_content))
