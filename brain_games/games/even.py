from brain_games.config import RULES
from brain_games.engine import game
from brain_games.random_number_gen import get_random_number


def even_rule():
    print(RULES['even'])


def is_even(num):
    return num % 2 == 0


def even_request():
    question = get_random_number()
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def even_game():
    game(even_rule, even_request)
