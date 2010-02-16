from Tkinter import *

class LifeGrid(Frame):
    
    def makeLiveCell(self, i, j):
        cell = Button(self.frame, bitmap="gray75", fg="red")
        cell.grid(column=i, row=j)
    
    def makeDeadCell(self, i, j):
        cell = Button(self.frame, bitmap="gray12")
        cell.grid(column=i, row=j)
        
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        
class GameBoard(Frame):
  
    def beginLife(self):
        self.start.pack_forget()

        #Initiate a new lifegrid in the parent window.        
        grid = LifeGrid(self.master)
        
        #Populate the new grid with dead cells.
        for i in range(self.width):
            for j in range(self.height):
                grid.makeDeadCell(i, j)
        
        

        
        
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

