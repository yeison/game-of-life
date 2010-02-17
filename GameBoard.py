#Written by Yeison Rodriguez
from LifeGrid import *
from random import randint

class GameBoard(Frame):

    #Creates a two dimensional array of zeros. (An empty life grid)
    def twoDArray(self, width, height):
        #Pad with  1 layer of cells, which never come to life
        return [[0 for i in range(height+1+1)] for i in range(width+1+1)]

    #Writes a new grid over the old one, then erases the old one.
    def updateGui(self, binaryGrid):
        oldgrid = self.grid
        self.grid = LifeGrid(self.frame)
        #Update the gui grid with data from the binary grid
        for i in range(self.width):
            for j in range(self.height):
                if(binaryGrid[i][j]):
                    self.grid.makeLiveCell(i, j)
                else:
                    self.grid.makeDeadCell(i, j)
        self.grid.pack()
        oldgrid.destroy()
  
    #When start is pressed, this initializes the first life grid using
    #random numbers.
    def beginLife(self):
        #Remove the start button
        self.start.pack_forget()

        #Binary arrays will represent life
        self.life = self.twoDArray(self.width, self.height)
        for i in range(1, self.width - 1):
            for j in range(1, self.height - 1):
                #Make the ones sparser (0*0 = 0, 0*1 = 0, 1*0 = 0, 1*1 = 1)
                self.life[i][j] = randint(0,1)*randint(0,1)
        
        #Prepare the binary grid of the next life
        self.nextLife = self.twoDArray(self.width, self.height)

        #Create the Next button
        next = Button(self.frame)
        next["text"] = "Next Life"
        next.pack(anchor=NE)        
        next["command"] = self.nextCycle
        
        #Initiate the first lifegrid (gui) in the parent window.        
        self.grid = LifeGrid(self.master)
        
        #Populate the grid with data from the first life(binary grid)
        self.updateGui(self.life)
        
        
    def nextCycle(self):
        #Get information about the next life, populate the next GUI
        #grid with that info.
        self.life = self.lifeCycle(self.life, self.nextLife)
        self.updateGui(self.life)        
        self.nextLife = self.twoDArray(self.width, self.height)

        
    def lifeCycle(self, life, nextLife):
        #Traverse every cell, find out if it is dead or alive.
        for i in range(1, self.width-1):
            for j in range(1, self.height-1):
                if(life[i][j]):
                    cell = LiveCell(i, j)
                    if(cell.isAliveNext(life)):
                        nextLife[i][j] = 1
                    else:
                        nextLife[i][j] = 0
                else:
                    cell = DeadCell(i, j)
                    if(cell.isAliveNext(life)):
                        nextLife[i][j] = 1
                    else:
                        nextLife[i][j] = 0
        return nextLife

                     
    def __init__(self, width, height):
        #When GameBoard is called, make a new Tk() window
        self.width = width
        self.height = height
        gameWindow = Tk()
        self.master = gameWindow
        gameWindow.title("Conway's Game of Life")
        dimensions = "+40+40"
        gameWindow.geometry(dimensions)

        self.frame = Frame(gameWindow)
        self.frame.pack()

        self.start = Button(self.frame)
        self.start["text"] = "Start"
        self.start["command"] = self.beginLife
        
        self.start.pack(anchor=CENTER)

        gameWindow.mainloop()
