#!/usr/bin/env python
"""
Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again
until the guess is correct, on successful guess, user will
get a "Well guessed!" message, and the program will exit.

Assumption:
    All user input are correct no.s
"""


from random import randint

print("Let's play a guessing game....")
print("Try guessing a number b/w 1 and 9 in not", end=" ")
print("more than 10 guesses")
num = int(input("[Enter a number]: "))
count = 1

ans = randint(1, 9)
while num != ans:
    if count < 5:
        if num < ans:
            print("Your guess is too low")
        elif num > ans:
            print("Your guess is too high")
        num = int(input("Try another guess: "))
        count += 1
    elif count == 5:
        print("You're out of guesses. Game over !!!")
        break
print("Well guessed")
