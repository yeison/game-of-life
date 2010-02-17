#!/usr/bin/env python
#This script runs Conway's Game of Life
#Requirements: Python 2.6 and Tcl/Tk (Most Linux systems have this).
#Run the script from a command line, and provide the board dimensions.
#Example: 'python conway.py 15 15'
#A 'Start' button will appear in the upper left corner of your screen.

from GameBoard import GameBoard
import sys

numberOfInputs = len(sys.argv)

if(numberOfInputs == 3 ):
    x = sys.argv[1]
    y = sys.argv[2]

#If the input is not 2 values, set default values.
else:
    x = 15
    y = 15


try:
    gameBoard = GameBoard(int(x), int(y))
#If the values cannot be cast to integers, set default values.
except ValueError as e:
    x = 15
    y = 15
    gameBoard = GameBoard(x, y)
