import prompt
import random

def main():
    def welcome_user():
        print("Welcome to the Brain Games!")
        name = prompt.string('May I have your name? ')
        return name

    def progression():
        shag = random.randint(1,6)
        l = [random.randint(0,10),]
        for i in range(10):
            l.append(l[i]+shag)
        found_element = l[random.randint(0,10)]
        l[l.index(found_element)] ='..'
        print(*l)
        user_answer = prompt.string('Your answer: ')
        if found_element == int(user_answer):
            print('Correct!')
            return 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{found_element}'.")
            print(f"Let's try again, {name}!")
            return 0


    
    name = welcome_user()
    print(f"Hello, {name}")
    print("What number is missing in the progression?")
    n = 0
    for i in range(3):
        if progression() == 0:
            break
        else:
            n+=1

    if n == 3:
        print(f"Congratulations, {name}!")
        
if __name__ == '__main__':
    main()