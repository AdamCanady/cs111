# Image Processing 3 by Adam Canady
# This program contains functions that will scale and blur images based on user input.

# When I tested the program, both functions ran under 2 seconds (on my personal
# MacBook Pro) with user inputs of 3 for scaling factor and 3 for blur radius.

# Additionally, the program will not run if the blur radius or scaling factor
# is less than or equal to zero or if the user does not choose "scale" or "blur"

# Grab the images library so we can do some stuff to photos
from images import *

# Define the function that will make pictures bigger or smaller, a.k.a. scale them
# It takes an image and a scaling factor.
def scale(image, scaling):
    # Provision to make sure user input makes sense.
    if scaling > 0:
        # Make some variables and a new image that will be the proper size based on
        # the scaling factor
        width = int(image.getWidth() * scaling)
        height = int(image.getHeight() * scaling)
        newImage = EmptyImage(width,height)
        # Loop over every pixel in the image by both width and height
        for i in range(width):
            for j in range(height):
                # Get the correct pixel from the old image. Basically we're going to see
                # what fraction of the new image dimension we're in and multiply that by
                # the width of the old image in order to get the corresponding pixel from
                # the old image.
                oldx = int(i * image.getWidth() / width)
                oldy = int(j *image.getHeight() / height)
                
                # Set the new pixel based on the correct pixel we just found out.
                newImage.setPixel2D(i,j,image.getPixel2D(oldx,oldy))
        # Return the newImage so we can claim this function works.
        return newImage        
    else:
        print "Enter a scaling factor that makes sense."


# Make a function that blurs images. It takes in an image and a blur radius.
def blur(image, radius):
    # Make a new image with the same dimensions as the old one so we can put
    # blurry stuff in it.
    width = image.getWidth()
    height = image.getHeight()
    newImage = EmptyImage(width,height)
    
    # Provision in case the user tries to enter 0 or a negative number.
    if radius > 0:
        # Loop over every pixel in the image by both width and heigth
        for i in range(width):
            for j in range(height):
                # Define some variables we'll use later.
                avg = (0,0,0)
                ravg = 0
                gavg = 0
                bavg = 0
                count = 0
                # Loop over the blur box and create a running average of values for
                # each pixel
                for a in range(i-radius,i+radius+1):
                    for b in range(j-radius,j+radius+1):
                        if a > 0 and b > 0 and (a < width and b < height):
                            # Counter, so we know how much to divide by for the average
                            count = count+1
                            r = image.getPixel2D(a,b)[0]
                            g = image.getPixel2D(a,b)[1]
                            b = image.getPixel2D(a,b)[2]
                            ravg = ravg + r
                            gavg = gavg + g
                            bavg = bavg + b
                # Put the averaged pixels in a tuple so we can utilize it
                avg = (int(ravg/count),int(gavg/count),int(bavg/count))
                # Set the new pixel to the average of it's surroundings within the radius
                newImage.setPixel2D(i,j,avg)
        # Give the image back so we can display it in main()
        return newImage
    else:
        print "Please enter a reasonable number."
    

    
def main():  
    # Grab the image from the file
    input = FileImage('davetiny.jpeg')
    
    # Have the user make a choice
    choice = raw_input('Would you like to scale or blur the image? (scale/blur) ')
    
    # Do different stuff depending on the choice
    if choice == 'scale':
        # Ask user for a scaling factor
        scaling = float(raw_input('What factor would you like to scale by? '))
        
        # Run the scale function and put the results in the variable updated
        updated = scale(input, scaling)
    elif choice == 'blur':
        # Ask the user for a blur radius
        radius = int(raw_input('What radius would you like to use? '))
        
        # Run the blur function and put the results in the variable updated
        updated = blur(input, radius)
    # Provision in case the user doesn't make sense.    
    else:
        print "Please make a choice that makes sense."
    
    # Show the original and the updated images so the user can compare.
    input.show('Original')
    updated.show('Updated')

    # Make the program wait so the user can see the images.
    raw_input('Check it out!')


# Run the function main() so the program actually does something
main()