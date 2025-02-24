from math import gcd

from brain_games.consts import RULES
from brain_games.engine import game
from brain_games.utils import get_random_number

RULES_GCD = RULES['gcd']


def get_question_and_answer():
    first_number, second_number = get_random_number(), get_random_number()
    answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, str(answer)


def gcd_game():
    game(RULES_GCD, get_question_and_answer)
