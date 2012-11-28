# input.py
# Written by Dave Musicant
# This program demonstrates how to accept input from the user.

currentString = raw_input('What is the current year? ')
currentyear = int(currentString)

birthString = raw_input('In what year were you born? ')
birthyear = int(birthString)

difference = currentyear - birthyear

print 'Hey! You\'re approximately', difference, 'years old!'