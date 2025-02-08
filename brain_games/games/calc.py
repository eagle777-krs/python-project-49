from random import choice

from brain_games.config import RULES
from brain_games.engine import game
from brain_games.random_number_gen import get_random_number


def calc_rule():
    print(RULES['calc'])


def calc_generating():
    operands = ['+', '-', '*']
    first_num = get_random_number()
    second_num = get_random_number()
    answer = 0
    operation = choice(operands)

    if operation == '+':
        answer = first_num + second_num
    elif operation == '-':
        answer = first_num - second_num
    elif operation == '*':
        answer = first_num * second_num

    return first_num, second_num, operation, answer


def calc_request():
    first_num, second_num, operation, answer = calc_generating()
    question = f'{first_num} {operation} {second_num}'
    correct_answer = str(answer)
    return question, correct_answer


def calc_game():
    game(calc_rule, calc_request)
