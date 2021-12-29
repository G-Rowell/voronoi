# Voronoi wikipedia: https://en.wikipedia.org/wiki/Voronoi_diagram
# W G Rowell

### Imports
from tkinter import *
from tkinter import ttk
import random
from v_classes import *

### Constants
numPoints = 10
points = []
edges = []

plotX = 500
plotY = 500

# random.seed(5)

root = Tk()
canvas = Canvas(root, width=plotX, height=plotY)
Point.xLimit = plotX
Point.yLimit = plotY

##########################################################
# Main
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
def delauny_triangulation():
    triangulation = []
    
##########################################################
# 
def gui():

    for myPoint in points:
        draw_point(myPoint)
    
    canvas.pack()
    
    log("finished GUI")
    root.mainloop()

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
