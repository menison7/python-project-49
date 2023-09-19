import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def even(name):
    list_answer = ['yes', 'no']
    n = random.randint(1, 100)
    print("Question:", n)
    answer = prompt.string('Your answer: ')
    if n % 2 == list_answer.index(answer.lower()):
        print('Correct!')
        return 1
    else:
        print(f''''{answer}' is wrong answer ;(. ''', end=" ")
        list_answer.remove(answer)
        print(f'''Correct answer was '{list_answer[0]}'.''')
        print(f"Let's try again, {name}!")
        return 0


def main():
    name = welcome_user()
    print(f"Hello, {name}")
    print('''Answer "yes" if the number is even, otherwise answer "no".''')
    n = 0
    for i in range(3):
        if even(name) == 0:
            break
        else:
            n += 1

    if n == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
