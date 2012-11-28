# Caesar Cipher Decoder by Adam Canady
# This decoder works with a space.

import string

# Get the user's input and desired code
# Open the file encrypted.txt and see what's up.
file = open('encrypted_space.txt','r')

# Put the first line of the file in a variable.
input = (file.readline()).rstrip('\n')
# Put the second line of the file in a variable.
key = (file.readline()).rstrip('\n')
key_len = len(key)
n = 0
final_string = ""

# Define the decoding function

def decode(letter_to_change):
    # Deal with spaces
    if ord(letter_to_change) == 32:
        ascii_input = 123
        ascii_key = ord(key[(n % key_len)]) - 97
        decoded_letter = ((ascii_input - ascii_key))
        if decoded_letter < 97:
            decoded_letter = encoded_letter + 27
        if decoded_letter == 123:
            decoded_letter = 32
    # If it's not a space, throw down some decoding magic
    else:
    
    # Alright, so we're going to need to grab the ASCII for the character we
    # want to decode, then add the ASCII of the code we want to change it by,
    # then assign that to decoded_letter so the function can return it.
    
        ascii_input = ord(letter_to_change)
        ascii_key = ord(key[(n % key_len)]) - 97
        decoded_letter = ((ascii_input - ascii_key))
        
        # But OMG, what if the decoded_letter is BELOW the alphabet?! Well,
        # throw another alphabet on it and everything will be O.K.
        if decoded_letter < 97:
            decoded_letter = decoded_letter + 27
        if decoded_letter == 123:
            decoded_letter = 32
    # And finally, the loop needs something back so it can seem like it's
    # doing work.
    return chr(decoded_letter)
  
  
# Iterate through the user's input letter by letter and change them
# using our decode function.
for letter in input:
    final_string += decode(letter)
    n = n + 1
    
print "Your decoded text is: " + final_string