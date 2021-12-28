# Voronoi wikipedia: https://en.wikipedia.org/wiki/Voronoi_diagram
# W G Rowell

### Imports
from tkinter import *
from tkinter import ttk
import random

### Constants
numPoints = 10
points = []
edges = []

plotX = 500
plotY = 500

random.seed(5)

root = Tk()
canvas = Canvas(root, width=plotX, height=plotY)

##########################################################
# Main
##########################################################

def main():
    root.geometry(f'{plotX}x{plotY}+500+500')
    
    ### Main algo
    log("Starting Voronoi generator")

    for i in range(numPoints):
        points.append(Point())
        
    log(f"numPoints = {numPoints}")
    # log(f"points = {points}")

    # delauny_triangulation(points)
    
        
    gui()

##########################################################
# 
# def delauny_triangulation():
#     triangulation = []
    
    
##########################################################
# 
def gui():

    for myPoint in points:
        draw_point(myPoint)
    
    canvas.pack()
    
    log("finished GUI")
    root.mainloop()

##########################################################
# Classes
##########################################################
class Point:
    def __init__(self, x = None, y = None):
        if x is None:
            self.xPos = random.randint(0,plotX)
        else:
            self.xPos = x
        
        if y is None:
            self.yPos = random.randint(0,plotY)
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

def draw_point(myPoint : Point):
    r = 20
    canvas.create_oval(myPoint.xPos-r, myPoint.yPos-r, myPoint.xPos+r, myPoint.yPos+r, fill='red')
    log(f"drew point: {myPoint}")

def draw_line(x, y, m):
    canvas.create_line(x, y, x+50, y+50)
    
##########################################################

if __name__ == '__main__':
    main()
    exit
