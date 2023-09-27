import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return name


def prime():
    name = welcome_user()
    print(f"Hello, {name}")
    n = 0
    print('''Answer "yes" if given number is prime. Otherwise answer "no".''')
    for i in range(3):
        list_pime = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]
        digit = random.randint(1, 100)
        print(f"Question: {digit}")
        user_answer = prompt.string('Your answer: ')
        if digit in list_pime and user_answer.lower() == 'yes':
            print('Correct!')
        elif digit not in list_pime and user_answer.lower() == 'no':
            print('Correct!')
        else:
            answer = ['yes', 'no']
            print(f''''{user_answer}' is wrong answer ;(. ''', end=" ")
            answer.remove(user_answer)
            print(f'''Correct answer was '{answer[0]}'.''')
            print(f"Let's try again, {name}!")
            break
        n += 1
        if n == 3:
            print(f"Congratulations, {name}!")


def main():
    prime()


if __name__ == '__main__':
    main()
