from random import randrange


# Write a program with the following features:
#
# - The program asks the user if they want a compliment: e.g.: "Do you want a
#     compliment?  y/n   :"
#
# - The user can enter multiple answers for postive_answers and muliple answers
#   for negative_answers. 
#
#   e.g.: 'sure' should be an accepted postive_answers 
#
# - [postive_answers]
#     - If the user requested a compliment, print a random compliment to the
#       screen. 
#
#       Hint: If you import randrange `from random import randrange` you can get
#       use `randrange(5)` to get a number from 0-4.
#
#     - Once you've printed the compliment. Ask the user again if they want a
#       compliment. This should continue until the user enters a
#       negative_answer. 
#
# - [negative_answers] 
#     - If the user enters a negative_answers, a message should be printed and
#       the program should stop. 
#
# *** BONUS ***  
# - [invalid answer]
#     - Use error handling to catch any other values (other than postive_answers
#       or negative_answers). In this case, a message should be printed to
#       indicate that the value entered is incorrect, and the user should be
#       asked if they want a compliment again.
#
#
# Hint: You can use `While(True)` to loop infinitely. BE CAREFUL. There must be
# an exit condition to your loop otherwise your program will go on forever!

postive_answers = ['y', 'yes', 'yup', 'sure']
negative_answers = ['n', 'no', 'nope', 'na']

compliments = ["You look great today.",
               "You're a smart cookie.",
               "I bet you make babies smile.",
               "You have impeccable manners.",
               "I like your style.",
               "You have the best laugh.",
               "I appreciate you.",
               "You’re strong."
               "Your perspective is refreshing.",
               "You’re an awesome friend.",
               "You light up the room.",
               "You deserve a hug right now.",
               "You should be proud of yourself.",
               "You’re more helpful than you realize.",
               "You have a great sense of humor.",
               "You’ve got all the right moves!",
               "Is that your picture next to “charming” in the dictionary?",
               "Your kindness is a balm to all who encounter it.",
               "You’re all that and a super-size bag of chips.",
               "On a scale from 1 to 10, you’re an 11.",
               "You are brave.",
               "You’re even more beautiful on the inside than you are on the outside.",
               "You have the courage of your convictions.", ]


while(True):
    wants_to_play = input("Do you want a compliment?  y/n   :")

    try:
        # Stop the loop
        if(wants_to_play.lower() in negative_answers):
            print("Too bad!\n")
            break

        # Raise error, go to `except block`
        elif wants_to_play.lower() not in postive_answers:
            raise ValueError('You must enter a proper value: y/n \n')

    # Run this code if there was an error in `try` block
    except ValueError as err:
        print(err)

        # go to next iteration of while loop
        continue

    # `try` block successful
    else:
        # print random compliment
        print(compliments[randrange(len(compliments))] + '\n')
