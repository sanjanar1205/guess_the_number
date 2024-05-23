import random

def guess_num_game():
    number = random.randint(1, 10)

    player_name = input("Hello, What's your name?\n")
    number_of_guesses = 0

    print("You have 3 chances to guess the number\n")
    print("Okay, " + player_name + "! I am guessing a number between 1 and 10:")

    while number_of_guesses < 3:
        guess = int(input("Your guess is: "))
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break

    if guess == number:
        print('Congratulations, ' + player_name + '! You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('Sorry, ' + player_name + ', you did not guess the number. The number was ' + str(number))

guess_num_game()
 