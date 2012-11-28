# Caeser Cipher Encoder by Adam Canady

import string

# Get the user's input and desired code
input = str.lower(raw_input("Type a phrase to encode: "))
key = str.lower(raw_input("Type the code you'd like to use: "))
key_len = len(key)
n = 0
final_string = ""

# Define the encoding function

def encode(letter_to_change):
    # Check for spaces and return a space
    if ord(letter_to_change) == 32:
        encodedLetter = 32
        
    # If it's not a space, throw down some encoding magic
    else:
    # Alright, so we're going to need to grab the ASCII for the character we
    # want to encode, then add the ASCII of the code we want to change it by,
    # then assign that to encoded_letter so the function can return it.
        ascii_input = ord(letter_to_change)
        print "letter_to_change = " + chr(ascii_input) + " - " + str(ascii_input)
        ascii_key = ord(key[(n % key_len)])
        print "code to change by = " + chr(ascii_key) + " - " + str(ascii_key)
        encodedLetter = ((ascii_input + ascii_key)) % 26 + 97
        print "encoded character: " + str(encodedLetter)
    return chr(encodedLetter)
  
  
# Iterate through the user's input letter by letter and change them
# using our encode function.
for letter in input:
    final_string = final_string + encode(letter)
    print encode(letter),
    n = n + 1
    
print ""
print final_string