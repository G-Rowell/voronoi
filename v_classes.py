# Voronoi wikipedia: https://en.wikipedia.org/wiki/Voronoi_diagram
# W G Rowell

# Helper & data structure classes for a voronoi generator
# Quaternary tree:
    # A ~4 leaf tree data structure to improve algo. O(_) time
    # also helps to make better guesses for points to start with
# Various geometry structures:
    # Points, triangles, polygons etc.

import random

##########################################################
# Classes
##########################################################
class Point:
    xLimit = 0
    yLimit = 0
    def __init__(self, x = None, y = None):
        if x is None:
            self.xPos = random.randint(0,Point.xLimit)
        else:
            self.xPos = x
        
        if y is None:
            self.yPos = random.randint(0,Point.yLimit)
        else:
            self.yPos = y
        
    def __str__(self):
        return f"xPos: {self.xPos}; yPos: {self.yPos}"
        
    def __repr__(self):
        return f"xPos: {self.xPos}; yPos: {self.yPos}"
    
class Triangle:
    def __init__(self, point1 : Point, point2: Point, point3 : Point):
        p1 = point1
        p2 = point2
        p3 = point3

##########################################################
# Helper functions
##########################################################

def log(message):
    print(message)
