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
        
class StartButton(Frame):
  
    def beginLife(self):
        self.start.pack_forget()

        #Initiate a new lifegrid in the parent window.        
        grid = LifeGrid(self.master)
        
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        
        self.start = Button(frame)
        self.start["text"] = "Start"
        self.start["command"] = self.beginLife
        
        self.start.pack(anchor=CENTER)
    

root = rootWindow = Tk()
start = StartButton(rootWindow)
    
root.geometry('300x200+40+40')

root.title("Conway's Game of Life")

root.mainloop()
