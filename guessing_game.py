import random
import time

print("Hello! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
print("Picking a number...")
time.sleep(1)
guess = int(input("Guess a number: "))
correct_answer = random.randint(1,100)
guess_count = 1

while guess != correct_answer:
  guess_count += 1
  if guess < correct_answer:
    guess = int(input("Too low! Please try again: "))
  else:
    guess = int(input("Too high! Please try again: "))

print(f"Congratulations! You guessed the correct number {correct_answer} in {guess_count} guesses.")

play_again = input("Would you like to play again? (y/n): ")

while play_again != "n":
  print("Picking a number...")
  time.sleep(1)
  guess = int(input("Guess a number: "))
  correct_answer = random.randint(1,100)
  guess_count = 1

  while guess != correct_answer:
    guess_count += 1
    if guess < correct_answer:
      guess = int(input("Too low! Please try again: "))
    else:
      guess = int(input("Too high! Please try again: "))

  print(f"Congratulations! You guessed the correct number {correct_answer} in {guess_count} guesses.")
  play_again = input("Would you like to play again? (y/n): ")
