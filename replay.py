import random
from hangman import main


def play_again():
    """
        If a valid response is give, it returns
        a string.If an invalid input is given,
        an invalid input message is given to the user.
    """
    answer = raw_input("would you like to play again?[y/n]").lower()
    if answer == 'y' or answer == 'n':
        if answer == 'y':
            hangman.main()
        elif answer == 'n':
            print "Thank you for playing"
            return 6
        else:
            print "Invalid input .... Thank you for playing?"
            return 6
    else:
        print" Invalid input of %s" % answer


def gallows(wrong_guess_count):
    """
        Takes one input and returns an ascii image
    """
    if wrong_guess_count == 0:

        print "\n"
        print "   __ "
        print "  |  |"
        print "  |   "
        print "  |   "
        print "  |   "
        print "  |   "
        print "------"
        print "|    |"

    elif wrong_guess_count == 1:
        print"\n"
        print "   __ "
        print "  |  |"
        print "  |  0"
        print "  |   "
        print "  |   "
        print "  |   "
        print "------"
        print "|    |"

    elif wrong_guess_count == 2:
        print"   __ "
        print"  |  |"
        print"  |  0"
        print"  |  |"
        print"  |   "
        print"  |   "
        print"------"
        print"|    |"

    elif wrong_guess_count == 3:
        print"   __ "
        print"  |  |"
        print"  |  0"
        print"  | /| "
        print"  |    "
        print"  |   "
        print"------"
        print"|    |"

    elif wrong_guess_count == 4:
        print"   __ "
        print"  |  |"
        print"  |  0"
        print"  | /|\ "
        print"  |   "
        print"  |   "
        print"------"
        print"|    |"

    elif wrong_guess_count == 5:
        print"   __ "
        print"  |  |"
        print"  |  0"
        print"  | /|\ "
        print"  | / "
        print"  |   "
        print"------"
        print"|    |"

    elif wrong_guess_count == 6:
        print"   __ "
        print"  |  |"
        print"  |  0"
        print"  | /|\ "
        print"  | / \ "
        print"  |   "
        print"------"
        print"|    |"


def Getword(word_list):
    """
        Takes one input and returns 2.
        Uses a random number to pick a
        word from the word list.
    """
    index_number = random.randrange(len(word_list))
    print word_list[index_number]
    word = "*"*len(word_list[index_number])
    return word, index_number


def match(userguess, word, hidden_word):
    """
        Takes 3 inputs and returns 2.Checks
        user's guess against each letter
        in the original word. If a match is found
        the hidden word is updated to show that you
        guessed a letter right.
    """
    i = 0
    count = 0
    middle_man = []
    for items in hidden_word:
        middle_man.append(items)
    while i < len(hidden_word):
        if userguess == word[i]:
            middle_man[i] = word[i]
            count += 1
        i += 1
    hidden_word = ""
    for items in middle_man:
        hidden_word += items
    if count > 0:
        return 0, hidden_word
    else:
        return 1, hidden_word


def wordsMatch(word, wordtoGuess):
    """
        Takes two inputs.
        Compares the hidden word with original word
        returns true if the words match or false if they don't
    """
    if word == wordtoGuess:
        return True
    else:
        return False
