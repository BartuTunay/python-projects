import random

choices = ["rock", "paper", "scissors"]
win_count = 0
tie_count = 0
lose_count = 0

while True:

    answer = random.choice(choices)
    guess = input("Rock, Paper or Scissors? also press q for exit: ").strip().lower()

    if guess == "q":
        break
    elif guess not in choices:
        print("Invalid Choice")
        continue
    print(f"Computer Choice: {answer}")
    
    if (guess == "rock" and answer =="scissors") or (guess == "scissors" and answer == "paper") or (guess == "paper" and answer == "rock"):
        print("Congratulations you Won! ")
        win_count += 1

    elif (guess == answer):
        print("That's a tie! ")
        tie_count += 1

    else:
        print("Computer Won! ")
        lose_count += 1    

print(f"Results:  Win: {win_count}  Lose: {lose_count}   Tie: {tie_count} ")        