from brain_games.main_logic import game
from random import randint

def prime_game():

    def rules():
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def request():
        question = randint(2, 300)
        correct_answer = 'yes'
        for division in range(2, question):
            if question % division == 0:
                correct_answer = 'no'
                return question, correct_answer
        return question, correct_answer
    
    game(rules, request)






