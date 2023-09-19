import prompt
import random

def main():
    def welcome_user():
        print("Welcome to the Brain Games!")
        name = prompt.string('May I have your name? ')
        return name

    def calc():
        a = random.randint(1,100)
        b = random.randint(1,100)
        z = random.randint(1,4)
        print("What is the result of the expression?")
        if z == 1:
            r = a + b
            print(f"Question: {a} + {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")
                return 1
            else:
                print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                return 0
        elif z == 2:
            r = a - b
            print(f"Question: {a} - {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")
                return 1
            else:
                print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                return 0
        else:
            r = a * b
            print(f"Question: {a} * {b}")
            user_answer = prompt.string('Your answer: ')
            if r == int(user_answer):
                print("Correct!")
                return 1
            else:
                print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{r}'.''')
                print(f"Let's try again, {name}!")
                return 0

    name = welcome_user()
    print(f"Hello, {name}")
    n = 0
    for i in range(3):
        if calc() == 0:
            break
        else:
            n+=1
    a = input().split()
    if n == 3:
        print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()


