import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def calc():
    name = welcome_user()
    print(f"Hello, {name}")
    ch = 0
    print("What is the result of the expression?")
    for i in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        z = random.randint(0, 2)
        z_l = ['-', '+', '*']
        rez = eval(str(a) + z_l[z] + str(b))
        print(f"Question: {a} {z_l[z]} {b}")
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == rez:
            print("Correct!")
        else:
            print(f''''{user_answer}' is wrong answer ;(.''', end='')
            print(f''' Correct answer was '{rez}'.''')
            print(f"Let's try again, {name}!")
            break
        ch += 1
        if ch == 3:
            print(f"Congratulations, {name}!")


def main():
    calc()


if __name__ == '__main__':
    main()
