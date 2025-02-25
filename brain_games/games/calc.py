from random import choice

from brain_games.consts import RULES
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def get_random_math_sign_and_result(first_num, second_num):
    return choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])


def get_math_question_and_result():
    first_num, second_num = get_random_number(), get_random_number()
    sign, answer = get_random_math_sign_and_result(first_num, second_num)
    question = f'{first_num} {sign} {second_num}'
    return question, str(answer)


def calc_game():
    run_game(RULES['calc'], get_math_question_and_result)
