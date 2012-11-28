# Recursion.py by Adam Canady
# Carleton College CS111 with Dave Musicant

# This program demonstrates knowledge of basic recursion and how to use it to break
# down problems.

# Define the palindrome-checker function. This will return True if a given input is
# a palindrome and False if it is not.
def palindrome(word):
    # Set up the base case
    if len(word) == 1:
        return True
    # Run through the word recursively to check if the first and last letters match   
    elif word[0] == word[len(word)-1]:
        return palindrome(word[1:(len(word)-1)])
    # If they don't match, return false because it's not a palindrome
    else:
        return False

# Define a function that takes a list as an input and throws out the max from that list        
def max(numberlist):
    # Define the base case, if we've taken out everything else from the list, give the
    # largest number back - which will be the only remaining number
    if len(numberlist) == 1:
        return numberlist[0]
    # Check recursively to see if the first number in the list is larger than the largest 
    # number in the rest of the list 
    if numberlist[0] >= max(numberlist[1:]):
        return numberlist[0]
    # If the first number wasn't larger, then eliminate it and redo the process
    # with the rest of the numbers in the list
    else:
        return max(numberlist[1:])
        
        
        
# Define a function main() that will test out our functions. Note: this is just an example
def main():
    # Define a list of numbers for our max function to use
    list = [102, 27, 16, 14, 93, 2, 170]
    
    # Make a palindrome and a not palindrome to test
    palindro = "racecar"
    none = "none"

    # Print the results from testing the functions
    print max(list)
    print palindrome(palindro)
    print palindrome(none)
    
# Run the program to see if it works!
main()