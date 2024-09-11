import random

def play():
    print("Welcome to the Guess the Number Game!")

    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()

    if difficulty == 'easy':
        max_attempts = 10
        number_range = 10
    elif difficulty == 'medium':
        max_attempts = 7
        number_range = 20
    else:  # Hard
        max_attempts = 5
        number_range = 50

    number = random.randint(1, number_range)
    attempts = 0
    score = 0

    print(f"I'm thinking of a number between 1 and {number_range}.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            score = (max_attempts - attempts + 1) * 10  # Score calculation based on remaining attempts
            print(f"Congratulations! You guessed the number in {attempts} attempts. Your score is {score}.")
            break

        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The number was {number}.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play()
