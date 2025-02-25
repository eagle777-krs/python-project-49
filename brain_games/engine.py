import prompt

from brain_games.consts import NUMBER_OF_ROUNDS


def run_game(rule, get_question_and_answer):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print(f'Hello, {name}!\n{rule}')

    for _ in range(NUMBER_OF_ROUNDS):

        question, correct_answer = get_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')
