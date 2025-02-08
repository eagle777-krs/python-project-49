from math import gcd

from brain_games.config import RULES
from brain_games.engine import game
from brain_games.random_number_gen import get_random_number


def gcd_rule():
    print(RULES['gcd'])


def gcd_generating():
    first_number = get_random_number()
    second_number = get_random_number()
    answer = str(gcd(first_number, second_number))
    return first_number, second_number, answer


def gcd_request():
    number1, number2, answer = gcd_generating()
    question = f'{number1} {number2}'
    return question, answer


def gcd_game():
    game(gcd_rule, gcd_request)
