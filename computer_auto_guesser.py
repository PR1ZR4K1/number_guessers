
import random


def main():

    # User initializes the upper and lower bounds for the
    # random number that the computer tries to guess
    lower_bound = int(input("What is the lower bound? "))
    upper_bound = int(input("What is the upper bound? "))

    # both guess and random_number manipulated by those bounds
    random_number = random.randint(lower_bound, upper_bound)
    computer_guess = random.randint(lower_bound, upper_bound)

    print(f'{random_number} the one you need to guess')

    # def auto_solve(prev_guess, low_bound, high_bound, high_low, computer_guess):
    #     prev_guess = computer_guess
    #     print(f'Computer guessed {computer_guess} and its too {high_low}')
    #     computer_guess = random.randint(low_bound, high_bound)

    # the while loop only covers the program if the first guess is wrong
    if (computer_guess == random_number):
        print("First Tryyyy")

    high_guess = 0
    low_guess = 0
    attempts = 0
    double_low = 0

    while (computer_guess != random_number):

        # if computer guesses too low twice in a row the second time the upper_bound (high_guess)
        # would be set to 0 which can't work
        if attempts > 0 and computer_guess < random_number and double_low > 0:
            low_guess = computer_guess
            print(f"Computer guessed {computer_guess} and its too low\n")
            computer_guess = random.randint((low_guess+1), (upper_bound))

        # now if the computer was wrong the bounds will have logic since we are storing the previous attempts
        elif attempts > 0 and computer_guess > random_number:
            high_guess = computer_guess
            print(f"Computer guessed {computer_guess} and its too high\n")
            computer_guess = random.randint((low_guess+1), (high_guess-1))
        # if the computer guessed too low we create a new guess making the new bounds in a way
        # to not repeat the previous attempt but also to not go past a previous attempts high guess
        elif attempts > 0 and computer_guess < random_number:
            low_guess = computer_guess
            print(f"Computer guessed {computer_guess} and its too low\n")
            computer_guess = random.randint((low_guess+1), (high_guess-1))
        else:
            # occurs for the computer's first guess.
            if computer_guess > random_number:
                print(f"Computer guessed {computer_guess} and its too high\n")
                high_guess = computer_guess
                computer_guess = random.randint(
                    lower_bound, (computer_guess-1))
            # the bounds that the computer can guess in changes if the computer guessed higher or lower.
            elif computer_guess < random_number:
                low_guess = computer_guess
                print(f"Computer guessed {computer_guess} and its too low\n")
                computer_guess = random.randint(
                    (computer_guess+1), upper_bound)
                double_low += 1

        attempts += 1

    print(f"Computer guessed {computer_guess}")
    print(f"Computer Wins!! It took {attempts+1} tries.")


if __name__ == "__main__":
    main()
