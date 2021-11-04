from random import randrange

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
