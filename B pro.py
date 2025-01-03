import random
def number_gguessing_game():
    secret_number = random.randint(1,100)
    attempts = 0
    while True:
        try:
            guess = int(input("guess a number between 1 to 100: "))
            attempts +=1
            if guess < secret_number:
                print("too low!")
            elif guess > secret_number:
                print("too high!")
            else:
                print(f"congratuiations! you guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("invalid input. please enter a number.")
number_gguessing_game()