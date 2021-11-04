# source: https://realpython.com/python-practice-problems/#python-practice-problem-2-caesar-cipher

# caesar.py
import string

def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    return plain_text.translate(trantab)


#  
plain_text = input('Text:   ')
shift_num = int(input('shift_num:   '))
print(caesar(plain_text,shift_num))