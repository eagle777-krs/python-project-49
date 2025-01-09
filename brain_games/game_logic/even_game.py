from random import randint
from brain_games.cli import welcome_user

def even_game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_points = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for round in range(3):
        number = randint(1, 100)

        print(f'Question: {number}')
        answer = input('Your answer: ')

        correct_answer = 'yes' if number % 2 == 0 else 'no'

        if answer == correct_answer:
            game_points += 1
            print('Correct!')
            if game_points == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break

