import random

print("----- Welcome to Guess Game -----")
answer = random.randint(1, 100)
guess_count = 0
while True:
    try:    
        guess = int(input("Guess a number between 1 - 100: "))
        guess_count += 1
        close = abs(guess - answer)
        if guess == answer:
            print("Wow Correct Answer!! ")
            print(f"Total Guesses: {guess_count}")
            break
        elif close <= 5:
            print("So Close Keep Guessing")
        elif close <= 15:
            print("Close enough")
        else:
            print("Incorrect Try Again")
    except ValueError:
        print("Oops Please Enter a valid Number")        
    