from brain_games.cli import welcome_user

def game(rule, request):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    number_of_rounds = 3

    rule()

    for _ in range(number_of_rounds):

        question, correct_answer = request()

        print(f'Question: {question}')
        answer = input(f'Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break
    else:
         print(f'Congratulations, {name}!')




