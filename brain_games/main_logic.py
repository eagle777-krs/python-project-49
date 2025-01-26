def game(rule, request):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    NUMBER_OF_ROUNDS = 3

    rule()

    for _ in range(NUMBER_OF_ROUNDS):

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
