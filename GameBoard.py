from LifeGrid import *
from random import randint

class GameBoard(Frame):


    def twoDArray(self, width, height):
        #Pad with  1 layer of cells, which never come to life
        return [[0 for i in range(height+1+1)] for i in range(width+1+1)]

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
  
    def beginLife(self):
        #Remove the start button
        self.start.pack_forget()

        #Binary arrays will represent life
        self.life = self.twoDArray(self.width, self.height)
        for i in range(1, self.width - 1):
            for j in range(1, self.height - 1):
                self.life[i][j] = randint(0,1)*randint(0,1)
        
        self.nextLife = self.twoDArray(self.width, self.height)

        #Initiate a new lifegrid (gui) in the parent window.

        next = Button(self.frame)
        next["text"] = "Next Life"
        next.pack(anchor=NE)        
        next["command"] = self.nextCycle
        
        self.grid = LifeGrid(self.master)
        
        self.updateGui(self.life)
        
        
    def nextCycle(self):
        self.life = self.lifeCycle(self.life, self.nextLife)
        self.updateGui(self.life)        
        self.nextLife = self.twoDArray(self.width, self.height)

        
    def lifeCycle(self, life, nextLife):
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
