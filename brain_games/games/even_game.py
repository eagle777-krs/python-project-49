from random import randint
from brain_games.cli import welcome_user

def brain_even_game():
        point_tracker = 0
        Flag = True
        name = welcome_user()

        while Flag == True:
                number = randint(1, 100)
                print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {number}')
                answer = input('Your answer: ')

                right_answer = 'yes' if number % 2 == 0 else 'no'

                if right_answer == answer:
                        point_tracker += 1
                        print('Correct!')
                                if point_tracker == 3:
                                        print(f'Congratulations, {name}!')
                                        Flag = False

                else:
                        print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
                        Flag = False
