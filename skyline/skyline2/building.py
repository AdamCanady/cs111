# Building.py by Adam Canady
# CS 111 with Dave Musicant, Fall 2012

# This program will define a class that will be used to generate
# random buildings to emulate a skyline.

# If you run this program, it should use graphics.py to display one small blue
# building on the left side of the graphics window.

# This code should cover everything from part 2 of the assignment.

# Import graphics.py because we'll need it!
from graphics import *

# Import the random library because we'll need it!
from random import *

# Create a cool Building class!

class Building:
    
    #Initialize some stuff when an instance is created!
    def __init__(self):
        self.height = 50
        self.width = 50
        self.location = 50
        self.color = 'black'
        
    # Set the object's variable height if the user gives one.
    def setHeight(self, h):
        self.height = h
    
    # Set the object's variable width if the user gives one.
    def setWidth(self, w):
        self.width = w
    
    # Set the object's variable color if the user gives one.
    def setColor(self, col):
        self.color = col
    
    # Set the object's variable location if the user gives one.
    def setHorizontalLocation(self, loc):
        self.location = loc
    
    # Draw the object.
    def draw(self, graphicsWindow, windowHeight):
        
        # Let's create something to put everything in.
        building = Rectangle(Point(self.location,windowHeight-self.height),Point(self.location + self.width, windowHeight))
        
        # Set that object's color correctly
        building.setFill(self.color)
        
        # Set that object's outline to the same color
        building.setOutline(self.color)
        
        # Lets do this.
        building.draw(graphicsWindow)
        
    ###########################################
    # Herein begins part 2 of the assignment! #
    ###########################################
        
    def setHeightRandom(self, maxHeight):
        self.height = randint(100,maxHeight)
    
    def setWidthRandom(self, maxWidth):
        self.width = randint(40,maxWidth)
    
    def setLocationRandom(self, maxLoc):
        self.location = randint(0, maxLoc)
        
    def setColorRandom(self):
        self.color = color_rgb(randint(0,255),randint(0,255),randint(0,255))
        
    def area(self):
        self.area = self.width * self.height
        return self.area


# Added debugging step just to see if everything works!     
if __name__ == '__main__':
    
    # Create a window object and make it appear
    windowWidth = 800
    windowHeight = 500
    window = GraphWin('Skyline',windowWidth,windowHeight)
    
    building = Building()
    building.setHeight(120)
    building.setWidth(windowWidth/5)
    building.setColor('blue')
    building.setHorizontalLocation(70)            
    building.draw(window,windowHeight)
    
    wait = raw_input("Press enter to continue")