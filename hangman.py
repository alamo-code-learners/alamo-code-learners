import time


name = raw_input("What is your name? ")

print "Hello %s, time to play hangman!\n" % name

time.sleep(1)

print "start guessing..."
time.sleep(0.5)

word = "secret"

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print char,
        else:
            print "-",
            failed += 1

    if failed == 0:
        print "\nYou won"
        break

    print

    guess = raw_input("guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1

        print "Wrong\n"

    print "You have %d more guesses" % turns

    if turns ==0:
        print "You Lose\n"
