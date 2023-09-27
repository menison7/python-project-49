import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def even():
    name = welcome_user()
    print(f"Hello, {name}")
    ch = 0
    print('''Answer "yes" if the number is even, otherwise answer "no".''')
    for i in range(3):
        list_answer = ['yes', 'no']
        n = random.randint(1, 100)
        print("Question:", n)
        answer = prompt.string('Your answer: ')
        if n % 2 == list_answer.index(answer.lower()):
            print('Correct!')

        else:
            print(f''''{answer}' is wrong answer ;(. ''', end=" ")
            list_answer.remove(answer)
            print(f'''Correct answer was '{list_answer[0]}'.''')
            print(f"Let's try again, {name}!")
            break
        ch += 1
        if ch == 3:
            print(f"Congratulations, {name}!")


def main():
    even()


if __name__ == '__main__':
    main()
