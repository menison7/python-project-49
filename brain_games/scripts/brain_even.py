import prompt
import random


def main():
    def welcome_user():
        print("Welcome to the Brain Games!")
        name = prompt.string('May I have your name? ')
        return name

    def even():
        l = ['yes','no']
        print('''Answer "yes" if the number is even, otherwise answer "no".''')
        n = random.randint(1,100)
        print("Question:",n)
        answer = prompt.string('Your answer: ')
        if n%2 == l.index(answer.lower()):
            print('Correct!')
            return 1
        else:
            print(f''''{answer}' is wrong answer ;(. ''',end = " ")
            l.remove(answer)
            print(f'''Correct answer was '{l[0]}'.''')
            print(f"Let's try again, {name}!")
            return 0


    name = welcome_user()
    print(f"Hello, {name}")

    n = 0
    for i in range(3):
        if even() == 0:
            break
        else:
            n+=1

    if n == 3:
        print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()


