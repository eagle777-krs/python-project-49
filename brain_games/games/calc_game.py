from random import choice, randint

from brain_games.main_logic import game


def calc_game():

	def rule():
		print('What is the result of the expression?')

	def request():
		operands = ['+', '-', '*']
		first_num = randint(1, 100)
		second_num = randint(1, 100)
		answer = 0
		operation = choice(operands)
		
		question = f'{first_num} {operation} {second_num}'
		
		if operation == '+':
			answer = first_num + second_num
		elif operation == '-':
			answer = first_num - second_num
		elif operation == '*':
			answer = first_num * second_num
		correct_answer = str(answer)
		
		return question, correct_answer
	
	game(rule, request)
