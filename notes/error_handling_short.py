try:
    number = int(input("Choose a number from 1-10:   "))

    if(number < 1 or number > 10):
        # Generic exception
        raise(Exception('{} is not in range 1-10'.format(number)))

except ValueError as err:
    print("That's not an int!")


except Exception as err:
    print(err)

else:
    print("{} is a great number".format(number))