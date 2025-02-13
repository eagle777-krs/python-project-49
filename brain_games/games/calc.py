from random import choice

from brain_games.consts import RULES
from brain_games.engine import game
from brain_games.utils import get_random_number


def calc_rule():
    print(RULES['calc'])


def calc_operation(num1, num2):
    operation = choice(['+', '-', '*'])
    operation_list = {'+': lambda a, b: a + b,
                      '-': lambda a, b: a - b,
                      '*': lambda a, b: a * b}

    return operation_list[operation](num1, num2), operation


def calc_data():
    first_num, second_num = get_random_number(), get_random_number()
    answer, operation = calc_operation(first_num, second_num)

    question = f'{first_num} {operation} {second_num}'
    correct_answer = str(answer)
    return question, correct_answer


def calc_game():
    game(calc_rule, calc_data)
