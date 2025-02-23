from random import choice

from brain_games.consts import RULES
from brain_games.engine import game
from brain_games.utils import get_random_number


def get_random_math_sign_and_result(first_num, second_num):
    sign, result = choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])
    return f'{first_num} {sign} {second_num}', result


def calc_get_question_and_answer():
    first_num, second_num = get_random_number(), get_random_number()
    question, answer = get_random_math_sign_and_result(first_num, second_num)
    return question, str(answer)


def calc_game():
    game(RULES['calc'], calc_get_question_and_answer)

