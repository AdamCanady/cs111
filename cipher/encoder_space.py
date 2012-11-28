# Caesar Cipher Encoder by Adam Canady
# This encoder works with a space.

import string

# Get the user's input and desired code
# Open the file source.txt and see what's up.
file = open('source_space.txt','r')

# Put the first line of the file in a variable.
input = (file.readline()).rstrip('\n')
# Put the second line of the file in a variable.
key = (file.readline()).rstrip('\n')
key_len = len(key)
n = 0
final_string = ""

# Define the encoding function

def encode(letter_to_change):
    # Check for spaces and deal with that
    if ord(letter_to_change) == 32:
        ascii_input = 123
        ascii_key = ord(key[(n % key_len)]) - 97
        encoded_letter = ((ascii_input + ascii_key))
        if encoded_letter > 123:
            encoded_letter = encoded_letter - 27
        elif encoded_letter == 123:
            encoded_letter = 32
    # If it's not a space, throw down some encoding magic
    else:
    # Alright, so we're going to need to grab the ASCII for the character we
    # want to encode, then add the ASCII of the code we want to change it by,
    # then assign that to encoded_letter so the function can return it.
        ascii_input = ord(letter_to_change)
        ascii_key = ord(key[(n % key_len)]) - 97
        encoded_letter = ((ascii_input + ascii_key))
        if encoded_letter > 123:
            encoded_letter = encoded_letter - 27
        elif encoded_letter == 123:
            encoded_letter = 32
    return chr(encoded_letter)
  
  
# Iterate through the user's input letter by letter and change them
# using our encode function.
for letter in input:
    final_string += encode(letter)
    n = n + 1
    
print "Your encoded text is: '" + final_string + "'"