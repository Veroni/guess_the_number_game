#Guess the number
import random

guesses_taken = 0
print("Hello! What is your name?")
my_name = input()
number = random.randint(1, 20)
print(my_name, ", I'm thinking of a number between 1 and 20.")

for i in range(6):
    print('Take a guess')
    guess = int(input())
    guesses_taken +=1
    if guess < number:
        print("Sorry, your guess is too low")
    elif guess > number:
        print("Sorry, your guess is too high")
    elif guess == number:
        print("Good job, " + my_name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
        break
