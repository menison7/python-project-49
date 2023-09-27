import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def progression():
    name = welcome_user()
    print(f"Hello, {name}")
    n = 0
    print("What number is missing in the progression?")
    for i in range(3):
        shag = random.randint(1, 6)
        list_prog = [random.randint(0, 10),]
        for i in range(10):
            list_prog.append(list_prog[i] + shag)
        found_element = list_prog[random.randint(0, 10)]
        list_prog[list_prog.index(found_element)] = '..'
        print("Question:", *list_prog)
        user_answer = prompt.string('Your answer: ')
        if found_element == int(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f"Correct answer was '{found_element}'.")
            print(f"Let's try again, {name}!")
            break
        n += 1
        if n == 3:
            print(f"Congratulations, {name}!")


def main():
    progression()


if __name__ == '__main__':
    main()
