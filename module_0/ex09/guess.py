import random

print("This is an interactive guessing game!\n"
"You have to enter a number between 1 and 99 to find out the secret number.\n"
"Type 'exit' to end the game.\n"
"Good luck!\n")

random.seed()
to_guess = random.randint(1, 99)
attempt = 0

while True:
    user_in = input("What's your guess between 1 and 99?\n")
    if user_in == "exit":
        print("Goodbye!")
        break
    try:
        user_in = int(user_in)
    except ValueError:
        print("That's not a number.")
        continue
    if user_in < 1 or user_in > 99:
        print("That's not in the range.")
        continue
    attempt += 1
    if user_in == 42:
        print("The answer to the ultimate question of life, "
              "the universe and everything is 42.")
    if user_in < to_guess:
        print("Too low!")
    elif user_in > to_guess:
        print("Too high!")
    else:
        if attempt == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!\n"
                  f"You won in {attempt} attempts!")
        break
