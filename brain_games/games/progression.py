from random import randint

from brain_games.config import RULES
from brain_games.engine import game
from brain_games.random_number_gen import get_random_number


def prog_rule():
    print(RULES['progression'])


def prog_request():
    progression = []
    current_number = get_random_number()
    gap = get_random_number()

    for _ in range(10):
        progression.append(str(current_number))
        current_number += gap

    index = randint(0, 9)
    correct_answer = str(progression.pop(index))

    progression.insert(index, '..')
    question = ' '.join(progression)

    return question, correct_answer


def progression_game():
    game(prog_rule, prog_request)
