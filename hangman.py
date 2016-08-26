import replay

# random list of words


def hangman():
    word_to_guess, word = replay.getWord() # word is the unaltered word
    wrong = 0
    end_game = True
    while end_game or wrong > 6:  # 6 is the number of wrong guess for the game ends
        replay.gallows(wrong)
        print word_to_guess  # used for test remove when finished
        users_guess = raw_input("Pick a letter you think the word contains:")
        if users_guess.isalpha():
            wrong_increment = 0
            wrong_increment, word_to_guess = replay.match(users_guess,
                                                        word, word_to_guess)
            wrong += wrong_increment  # not very clear on what it is for
        else:
            print "Invalid input!"
            wrong += 1
        victory = replay.wordsMatch(word, word_to_guess)
        if wrong == 6:
            replay.gallows(wrong)
            print word_to_guess
            print "You lose"
            end_game = False
        elif victory:
            print "You won!\n"
            end_game = False


def main():
    """
        If a valid response is give, it returns
        a string.If an invalid input is given,
        an invalid input message is given to the user.
    """
    play = True
    while play:
        answer = raw_input("Would you like to play hangman?[yes/no]").lower()
        if answer == 'yes':
            hangman()
        elif answer == 'no':
            print "Thank you for playing"
            return False
        else:
            print "Invalid input .... Thank you for playing?"
            return False


if __name__ == "__main__":
    print "Welcome to Hangman!"
    main()
