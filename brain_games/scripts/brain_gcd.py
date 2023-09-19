import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def gcd(name):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    nd = 0
    print(f"Question: {min(a,b)} {max(a,b)}")

    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            nd = i
    user_answer = prompt.string('Your answer: ')
    if nd == int(user_answer):
        print('Correct!')
        return 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{nd}'.")
        print(f"Let's try again, {name}!")
        return 0


def main():
    name = welcome_user()
    print(f"Hello, {name}")
    print("Find the greatest common divisor of given numbers.")
    n = 0
    for i in range(3):
        if gcd(name) == 0:
            break
        else:
            n += 1

    if n == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
