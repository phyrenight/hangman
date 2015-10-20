import random
import replay
word_list = ["time", "travel", "people", "fart",
             "town", ]
# random list of words


def main():
    wordtoGuess, index_number = replay.Getword(word_list)
    word = word_list[index_number]  # unaltered word to guess
    wrong = 0
    while wrong < 6:
        replay.gallows(wrong)
        print wordtoGuess
        usersGuess = raw_input("Pick a letter you think the word contains:")
        if usersGuess.isalpha():
            wrong_increment = 0
            wrong_increment, wordtoGuess = replay.match(usersGuess,
                                                        word, wordtoGuess)
            wrong += wrong_increment
        else:
            print "Invalid input!"
            wrong += 1
        victory = False
        victory = replay.wordsMatch(word, wordtoGuess)
        if wrong == 6:
            replay.gallows(wrong)
            print wordtoGuess
            print "You lose"
            wrong = replay.play_again()
        elif victory:
            print "You won!\n"
            wrong = replay.play_again()

if __name__ == "__main__":
    print "Welcome to Hangman!"
    main()
