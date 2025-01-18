from brain_games.main_logic import game
from random import randint

def nod_game():

	def rule():
		print('Find the greatest common divisor of given numbers.')

	def request():
		first_number = randint(1,100)
		second_number = randint(1,100)
		question = f'{first_number} {second_number}'
		
		if second_number > first_number:
			first_number, second_number = second_number, first_number
		
		while second_number != 0:
			first_number, second_number = second_number, first_number % second_number
		correct_answer = str(first_number)

		return question, correct_answer
	
	game(rule, request)
