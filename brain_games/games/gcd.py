from math import gcd

from brain_games.consts import RULES
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def get_question_and_answer():
    first_number, second_number = get_random_number(), get_random_number()
    answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, str(answer)


def gcd_game():
    run_game(RULES['gcd'], get_question_and_answer)
