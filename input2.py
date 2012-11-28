# input.py
# Written by Dave Musicant
# This program demonstrates how to accept input from the user.

name = raw_input('What is your name? ')

ageString = raw_input('How old are you? ')
age = int(ageString)

print 'Hi,', name, '.'
print 'The square of your age is', age * age