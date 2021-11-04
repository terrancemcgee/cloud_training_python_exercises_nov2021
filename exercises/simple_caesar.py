
# Replace each letter in the string by the letter `shift_num` away from it. 
# When the end of alphabet is reached, it returns back to the beginning.

def simple_caesar(text, shift_num):
    # final string 
    result = ""

    for letter in text:
        # number representation of the lower case letter
        ascii_val = ord(str(letter).lower())

        # increment ascii value 
        new_ascii_val = ascii_val + shift_num
        
        # if the new ascii value is greater than z's ascii value loop back to 'a' 
        if new_ascii_val > ord('z'):
            new_ascii_val -= 26
        
        # convert new_ascii_val back to a letter 
        new_letter = chr(new_ascii_val)
        
        # add new letter to final string
        result += new_letter
    
    return result


plain_text = input('Text:   ')
shift_num = int(input('shift_num:   '))
print(simple_caesar(plain_text,shift_num))


