from random import randint
from brain_games.main_logic import game

def even_game():
	
	def rule():
		 print('Answer "yes" if the number is even, otherwise answer "no".')

	def request():
		question = randint(1, 100)
		correct_answer = 'yes' if question % 2 == 0 else 'no'
		return question, correct_answer
	
	game(rule, request)
