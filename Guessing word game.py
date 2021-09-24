number = 45
attempts = 0

while True :
    attempts += 1

    guess = int(input("Enter the number you guessed: "))
    if guess < number:
        print("your guess is too Low!")
    elif guess > number:
        print("your guess is too High!")
    else:
        print(" Congratulation your guess is right!")
        print(f"you have guessed the number at {attempts} attempts")
        break

print("Thanks for playing!")

