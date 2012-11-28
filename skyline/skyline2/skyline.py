# Skyline.py by Dave Musicant

# Note from Adam Canady - this code was used to test the class in building.py

from building import *
from graphics import *

def main():
    # Create a window object and make it appear
    windowWidth = 800
    windowHeight = 500
    window = GraphWin('Skyline',windowWidth,windowHeight)
    
    # Generate 50 building objects, and draw each one.
    # Sum up the area as you go along.
    totalArea = 0        
    for i in range(50):
        building = Building()
        building.setHeightRandom(windowHeight)
        building.setWidthRandom(windowWidth/5)
        building.setColorRandom()
        building.setLocationRandom(windowWidth)            
        building.draw(window,windowHeight)
        totalArea = totalArea + building.area()
        
    # Display results.
    print "Total area =", totalArea
    
    raw_input("Press enter when done")
    window.close()

main()
