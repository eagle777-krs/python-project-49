from random import randint

from brain_games.consts import RULES
from brain_games.engine import game
from brain_games.utils import get_random_number


def prog_get_question_and_answer():
    progression = []
    first_num = get_random_number()
    diff = get_random_number()

    for _ in range(10):
        progression.append(str(first_num))
        first_num += diff

    missed_number_id = randint(0, 9)
    correct_answer = str(progression.pop(missed_number_id))

    progression.insert(missed_number_id, '..')
    question = ' '.join(progression)

    return question, correct_answer


def progression_game():
    game(RULES['progression'], prog_get_question_and_answer)
