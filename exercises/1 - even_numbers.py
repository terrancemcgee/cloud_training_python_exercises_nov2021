# Python program to print Even Numbers in a List.
# Use a function and a loop.

def get_even_numbers(int_list):
    even_numbers = []

    # iterating each number in list
    for num in int_list:

        # checking condition
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


# list of numbers
int_list = [10, 21, 4, 45, 66, 93]
print(get_even_numbers(int_list))
