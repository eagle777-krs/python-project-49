from brain_games.consts import RULES
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def is_even(num):
    return num % 2 == 0


def get_answer_and_question():
    question = get_random_number()
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def even_game():
    run_game(RULES['even'], get_answer_and_question)
