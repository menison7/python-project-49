import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def gcd():
    name = welcome_user()
    print(f"Hello, {name}")
    n = 0
    print("Find the greatest common divisor of given numbers.")
    for i in range(3):
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
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{nd}'.")
            print(f"Let's try again, {name}!")
            break
        n += 1
        if n == 3:
            print(f"Congratulations, {name}!")


def main():
    gcd()


if __name__ == '__main__':
    main()
