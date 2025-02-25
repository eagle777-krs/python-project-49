from math import sqrt

from brain_games.consts import RULES
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True


def get_question_and_answer():
    question = get_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def prime_game():
    run_game(RULES['prime'], get_question_and_answer)
