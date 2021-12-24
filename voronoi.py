# Voronoi wikipedia: https://en.wikipedia.org/wiki/Voronoi_diagram
# W G Rowell

### Imports
from tkinter import *
import random

### Constants
numPoints = 10
points = []

plotX = 500
plotY = 500

random.seed(5)

##########################################################
# Main body
##########################################################

def main():
    ### Main algo
    log("Starting Voronoi generator")
    
    for x in range(numPoints):
        point = [random.randint(0, plotX), random.randint(0, plotY)]
        points.append(point)
    
    print(points)

##########################################################
# Helper functions
##########################################################

def log(message):
    print(message)
    
##########################################################

if __name__ == '__main__':
    main()
    exit
