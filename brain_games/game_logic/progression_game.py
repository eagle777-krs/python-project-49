from brain_games.main_logic import game
from random import randint

def progression_game():
    
    def rule():
        print('What number is missing in the progression?')

    def request():
        progression = []
        current_number = randint(1, 100)
        gap = randint(1, 100)

        for _ in range(10):
            progression.append(str(current_number))
            current_number += gap

        index = randint(0, 9)
        correct_answer = str(progression.pop(index))

        progression.insert(index, '..')
        question = ' '.join(progression)

        return question, correct_answer

    game(rule, request)



