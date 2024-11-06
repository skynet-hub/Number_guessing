from operators import *
from random import randint

print('welcome to the number guessing game: ')
input('Do you want to a play a round of the number_guessing game? "y" to play and "n" to exit: ')

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

symbols = ['+', '-', '*', '/']
operator = input('Which operator will you like to play using? ("+". "-", "*", "/"): ')
while operator not in symbols:
    print("***Enter a valid operator*****")
    print("\n")
    operator = input('Which operator will you like to play using? ("+". "-", "*", "/"): ')

counter = 0

for symbol in operators:
    if operator == symbol:
        for index in range(5):
            total = index + 1
            num1 = randint(1, 100)
            num2 = randint(1, 100)
            while True:
                try:
                    print("\n")
                    Q = int(input(f'What is the answer to {num1} {symbol} {num2}: '))
                    break
                except ValueError:
                    print("*******Enter a number*********")
                    print("\n")

            if Q == operators[symbol](num1, num2):
                counter += 1
                print("You got it right!!")
                print(f"Your score: {counter}/{total}")
            else:
                print("Unfortunately You did not get this round correct, try do better next round")
                print(f"Your score: {counter}/{total}")
            print(f"The right answer was {operators[symbol](num1, num2)}")            
            print("\n")

print(f"Your final score is: {counter}/{total}")