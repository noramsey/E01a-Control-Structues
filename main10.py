#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') (#Print displays the text inside the parenthesis and '')
colors = ['red','orange','yellow','green','blue','violet','purple'] (#the text in the brackets is now codified to be synonomous with the word 'colors')
play_again = '' #i'm beginning to the think '' means anything typed as an input
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #while constantly checks to see if play_again's condition is not met, as either n or no because n is a shorthand for no
    match_color = random.choice(colors) #the correct color is sampled from the pool above where colors = (X), and the random.choice dictates the match color, well, randomly
    count = 0 #keeps a running total of a number
    color = '' #color now equals text, not a variable, I think
    while (color != match_color): (# if the color does not equal the correct colors it will do the things listed below)
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line 
        color = color.lower().strip() #lower and strip ensure that spacing and capitalization won't make inputs incorrect
        count += 1 (#adds one to count evey time color != match_color )
        if (color == match_color): #condition if color entered is correct, enacting next sequence below)
            print('Correct!') #enacts if condition is met above, showing text
        else: #condition if color != match_color, enacting ext below.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #print displays text in parenthesis while guesses is changed based on count, because guesses = count
    print('\nYou guessed it in {0} tries!'.format(count)) (#displays text showing how many times you've guessed if play_again = n)
    if (count < best_count): (#best count is the fewest number of times the user has needed to guess the correct color, this condition says if count is less than bestcount to enact the condition below)
        print('This was your best guess so far!') #it will display the text when the perameters are met above
        best_count = count #tracks count relative to best count 
    play_again = input("\nWould you like to play again? ").lower().strip() #prompts user to answer n, with all other possible anwers being 'Yes', if yes is the answer, the code will go through the above actions again
print('Thanks for playing!') #displays only if playagain = no