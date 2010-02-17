from Tkinter import *
from math import sin, cos, pi, sqrt
import sys

class LifeGrid(Frame):
    
    def makeLiveCell(self, i, j):
        cell = Button(self.frame, bitmap="gray75", fg="red")
        cell.grid(column=i, row=j)
        #self.nextLife[i, j] = 1
    
    def makeDeadCell(self, i, j):
        cell = Button(self.frame, bitmap="gray12")
        cell.grid(column=i, row=j)
        #self.nextLife[i, j] = 0
        
    def __init__(self, master, binaryGrid):
        self.frame = Frame(master)
        self.frame.pack()


class Cell:

    def probeNeighbors(self, binaryGrid):
        self.neighbors = 0
        for i in range(8):
            d = 1
            if(i%2):
                d = sqrt(2)
            theta = (i*pi)/4
            x = self.i + d*cos(theta)
            y = self.j + d*sin(theta)

            #If the neighbor at x,y is alive
            if(binaryGrid[x, y]):
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
    def isAliveNext(self, grid):
        neighbors = self.probeNeighbors(binaryGrid)
        if(neighbors == 3):
            return True
        

class GameBoard(Frame):

    def 2dArray(width, height):
        #Pad with  1 layer of cells, which never come to life
        return [[0 for i in range(height+1+1)] for i in range(width+1+1)]
  
    def beginLife(self):
        #Remove the start button
        self.start.pack_forget()

        #Binary arrays will represent life
        life = 2dArray(self.width, self.height)
        nextLife = 2dArray(self.width, self.height)

        #Initiate a new lifegrid (gui) in the parent window.        
        grid = LifeGrid(self.master, self.width, self.height)
        
        #Populate the new grid with initial conditions
        for i in range(self.width):
            for j in range(self.height):
                grid.makeDeadCell(i, j)

        for i in range(1, self.width-1):
            for j in range(1, self.height-1):
                if(life[i][j]):
                    cell = LiveCell(i, j)
                    if(cell.isAliveNext(life)):
                        nextLife[i][j] = 1
                        grid.makeLiveCell(i, j)
                else:
                    cell = DeadCell(i, j)
                    if(cell.isAliveNext(life)):
                        nextLife[i][j] = 1
                        grid.makeLiveCell(i, j)

                    
    
        
                
    def __init__(self, width, height):
        self.width = width
        self.height = height
        gameWindow = Tk()
        self.master = gameWindow
        gameWindow.title("Conway's Game of Life")
        dimensions = "+40+40"
        gameWindow.geometry(dimensions)

        frame = Frame(gameWindow)
        frame.pack()

        self.start = Button(frame)
        self.start["text"] = "Start"
        self.start["command"] = self.beginLife
        
        self.start.pack(anchor=CENTER)

        gameWindow.mainloop()
