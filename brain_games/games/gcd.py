from math import gcd

from brain_games.consts import RULES
from brain_games.engine import game
from brain_games.utils import get_random_number


def gcd_rule():
    print(RULES['gcd'])


def gcd_data():
    first_number, second_number = get_random_number(), get_random_number()
    answer = str(gcd(first_number, second_number))
    question = f'{first_number} {second_number}'
    return question, answer


def gcd_game():
    game(gcd_rule, gcd_data)
