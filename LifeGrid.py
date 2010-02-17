from Tkinter import *
from math import sin, cos, pi, sqrt
import sys

class LifeGrid(Frame):
    
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

    def probeNeighbors(self, binaryGrid):
        self.neighbors = 0
        for i in range(8):
            d = 1
            if(i%2):
                d = sqrt(2)
            theta = (i*pi)/4
            x = int(self.i + d*cos(theta))
            y = int(self.j + d*sin(theta))
            #If the neighbor at x,y is alive
            if(binaryGrid[x][y]):
                #increase number of neighbors
                self.neighbors += 1
                if(self.neighbors > 8):
                    print >> sys.stderr, "Too many neighbors."

        return self.neighbors
                        
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.neighbors = 0


class LiveCell(Cell):
    def isAliveNext(self, binaryGrid):
        neighbors = self.probeNeighbors(binaryGrid)
        if(neighbors < 2 or neighbors > 3):
            return False
        if(2 <= neighbors <= 3):
            return True


class DeadCell(Cell):
    def isAliveNext(self, binaryGrid):
        neighbors = self.probeNeighbors(binaryGrid)
        if(neighbors == 3):
            return True
        else:
            return False
