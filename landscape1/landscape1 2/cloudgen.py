# Written by Adam Canady
# CS 111 Fa2012 with Dave Musicant

# Grab the graphics library

from graphics import *

# Get user's responses for windspeed and time elapsed

windspeedR = raw_input('What is the windspeed in Miles per Hour (MPH)? ')
# Make windspeedR a float so decimal numbers work
windspeed = float(windspeedR)
timeelapsedR = raw_input('How much time has elapsed in hours? ')
# Make timeelapsedR a float so decimal numbers work
timeelapsed = float(timeelapsedR)

# Since the canvas is 500 px wide which equals 20 miles
# this means that there are 25 pixels per mile

# We need to use this value to determine the starting location
# for the clouds.

# Since Distance = Rate * Time
# We can extrapolate that 
# location (distance the cloud traveled) = windspeed (rate) * timeelapsed (time)
# then multiply by 25 ( * 25 ) to convert to pixels (using stoichiometry,
# the miles cancel)

location = windspeed * timeelapsed * 25

# We can't have clouds start on partial pixels!

location = round(location)

# Make a Canvas with dimensions 500 wide x 700 tall

canvas = GraphWin('Landscape', 500, 700)
canvas.setBackground('blue')

# Draw some buildings

building1 = Rectangle(Point(20, 350), Point(150, 500))
building1.setFill('black')
building1.draw(canvas)

building2 = Rectangle(Point(300, 400), Point(480, 500))
building2.setFill('black')
building2.draw(canvas)

# Draw the ground

ground = Rectangle(Point(0, 500), Point (500, 700))
ground.setFill('green')
ground.draw(canvas)

# Draw the clouds
cloud1 = Oval(Point(location, 20), Point(location+80, 50))
cloud1.setFill('white')
cloud1.setOutline('white')
cloud1.draw(canvas)

cloud2 = Oval(Point(location+15, 10), Point(location+95, 40))
cloud2.setFill('white')
cloud2.setOutline('white')
cloud2.draw(canvas)

# Draw a couple more clouds

cloud3 = Oval(Point(location+200, 50), Point(location+300, 100))
cloud3.setFill('white')
cloud3.setOutline('white')
cloud3.draw(canvas)

cloud4 = Oval(Point(location+230, 80), Point(location+340, 140))
cloud4.setFill('white')
cloud4.setOutline('white')
cloud4.draw(canvas)

# Wait for user input so we can see what we've done.

raw_input("Hit Enter to Continue")
