import random, time

# List of words that will be used for that game
words = ['bubbles', 'time', 'apple', 'banana', 'baby',
         'vision', 'crying', 'robot', 'toilet', 'whip',
         'whatever', 'shooter', 'ambidextrous', 'arbitration']

# States of the game
player_guess_list = []
player_guesses = []
play_game = True
category = ''
continue_game = 'Y'

# Start of the Game notation and intro
name = input("Enter your name")
print("Hello " + name.capitalize() + " let's start playing Hangman!")
time.sleep(1)
print("The Objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(2)
print("Let the game begin")
time.sleep(1)

while True:
    secretWord = random.choice(words)

    if play_game:
        secret_word_list = list(secretWord)
        attempts = (len(secretWord) + 2)

        # Print Player Guess List
        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(player_guess_list))

        # add blank lines
        for i in secret_word_list:
            player_guess_list.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", attemps)

        # start the game
        while True:

            print("Guess a letter")
            letter = input()

            if letter in player_guesses:
                print("You already guessed this letter, try again")

            else:
                attempts -= 1
                player_guesses.append(letter)
                if letter in secret_word_list:
                    print("Correct Guess!")
                    if attempts > 1:
                        print("You have ", attempts, 'guesses left.')
                    elif attempts == 1:
                        print("This is your final guess")
                    for i in range(len(secret_word_list)):
                        if letter == secret_word_list[i]:
                            letterIndex = i
                            player_guess_list[i] = letter.upper()

                    printGuessedLetter()

                else:
                    print("Incorrect Guess!")
                    if attempts > 1:
                        print("You have ", attempts, 'guesses left.')
                    elif attempts == 1:
                        print("This is your final guess")
                    printGuessedLetter()


            # win/loss logic
            joined_list = ''.join(player_guess_list)
            if joined_list.upper() == secretWord.upper():
                print("You win the game!")
                break
            elif attempts == 0:
                print("You're all out of guesses you lose!")
                print("The secret word was: " + secretWord.upper())
                break

        # play again
        continue_game = input("Do you want to play again? Y to continue, any other key to end")
        if continue_game.upper() == 'Y':
            player_guess_list = []
            player_guesses = []
            play_game = True
        else:
            print("Thank you for playing.")
            break
    else:
        break