import random



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


def getWord():
    """
        Takes one input and returns 2.
        Uses a random number to pick a
        word from the word list.
    """
    word_list = ["time", "travel", "people", "fart",
             "town", ]
    index_number = random.randrange(len(word_list))
    print word_list[index_number]
    word = "*"*len(word_list[index_number])
    return word, word_list[index_number]


def match(user_guess, word, hidden_word):
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
        if user_guess == word[i]:
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


def wordsMatch(word, word_to_Guess):
    """
        Takes two inputs.
        Compares the hidden word with original word
        returns true if the words match or false if they don't
    """
    if word == word_to_Guess:
        return True
    else:
        return False
