import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def calc():
    name = welcome_user()
    print(f"Hello, {name}")
    n = 0
    print("What is the result of the expression?")
    for i in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        z = random.randint(1, 4)
        if z == 1:
            r = a + b
            print(f"Question: {a} + {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")

            else:
                print(f''''{user_answer}' is wrong answer ;(.''', end='')
                print(f''' Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                break
        elif z == 2:
            r = a - b
            print(f"Question: {a} - {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")

            else:
                print(f''''{user_answer}' is wrong answer ;(.''', end='')
                print(f''' Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                break
        else:
            r = a * b
            print(f"Question: {a} * {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")

            else:
                print(f''''{user_answer}' is wrong answer ;(.''', end='')
                print(f''' Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                break
        n += 1
        if n == 3:
            print(f"Congratulations, {name}!")


def main():
    calc()


if __name__ == '__main__':
    main()
