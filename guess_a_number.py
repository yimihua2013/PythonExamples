# Guess_a_number Game

from random import randint

# welcome info & game rule
print("Welcome to the game!")
rules = """ 
Game rules:
(1)First, the program will randomly choose a numer from 1 to 10;
(2)Next, you bets a guess, if the guess is right, you win, otherwise, you lose. 
(3)In total, you have 3 chances to win.
"""
print(rules)
print("Good luck!")

# choose a random integer in 1 to 10
theNumber = randint(1,10) 

# 3 times for player to guess
times = 3

# use while/else loop to implement the game
while times > 0:
	 guess = int(raw_input("Your guess:"))
	 if guess == theNumber:
	 	print ("You are awsome,you win!")
	 	break
	 times -= 1
else:
	print ("You lose! The right number is : " + str(theNumber))
     
