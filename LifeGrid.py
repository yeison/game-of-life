from Tkinter import *
from math import sin, cos, pi, sqrt
import sys

class LifeGrid(Frame):
#Lifegrid is a subclass of Tkinter.Frame(Gui).  It contains the methods
#to display dead(gray) and live(red) "cell", which are actually just
#Tkinter.Buttons.  These buttons slow down the program substantially for 
#grids larger than 20x20.  But they look nice for this application.
    def makeLiveCell(self, i, j):
        cell = Button(self, bitmap="gray75", fg="red")
        cell.grid(column=i, row=j)
        #self.nextLife[i, j] = 1
    
    def makeDeadCell(self, i, j):
        cell = Button(self, bitmap="gray12")
        cell.grid(column=i, row=j)
        #self.nextLife[i, j] = 0
        
    def __init__(self, master=None):
        Frame.__init__(self, master)


class Cell:
#This class contains the core algorithm to solve the game of life problem
    def probeNeighbors(self, binaryGrid):
        self.neighbors = 0
        for i in range(8):
            d = 1
            #If i is odd theta is diagonal to the axes
            if(i%2):
                d = sqrt(2)
            #Instead of pi, use a truncated estimate to increase processing speed.
            theta = (i*3.1416)/4
            #Instead of hard coding x+1 y+1 etc.., I thought we should take
            #advantage of the fact that the grid is a euclidean plane
            x = int(self.i + round(d*cos(theta)))
            y = int(self.j + round(d*sin(theta)))
            #If the neighbor at x, y is alive
            if(binaryGrid[x][y]):
                #increase number of neighbors
                self.neighbors += 1
                if(self.neighbors > 8):
                    #Just in case.
                    print >> sys.stderr, "Too many neighbors."

        return self.neighbors
                        
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.neighbors = 0


class LiveCell(Cell):
#Subclass of Cell.  Defines isAliveNext for live cells.
    def isAliveNext(self, binaryGrid):
        #Use to ask if this cell is alive next life.
        neighbors = self.probeNeighbors(binaryGrid)
        if(neighbors < 2 or neighbors > 3):
            return False
        if(2 <= neighbors <= 3):
            return True


class DeadCell(Cell):
#Subclass of Cell.  Defines isAliveNext for dead cells.
    def isAliveNext(self, binaryGrid):
        neighbors = self.probeNeighbors(binaryGrid)
        if(neighbors == 3):
            return True
        else:
            return False
