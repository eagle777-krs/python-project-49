from math import sqrt

from brain_games.config import RULES
from brain_games.engine import game
from brain_games.random_number_gen import get_random_number


def prime_rule():
    print(RULES['prime'])


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True


def prime_request():
    question = get_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def prime_game():
    game(prime_rule, prime_request)





