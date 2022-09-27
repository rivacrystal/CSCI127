#Name: Riva Crystal
#Email: riva.crystal@gmail.com
#Date: November 3, 2021
#This program makes a checkerboard

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import turtle


# create a numpy checkerboard and save it
def drawBoard(size):
   board = np.ones((size,size,3))
   board[1::2,::2,:] = 1
   board[::2,1::2,:] = 1  
   
   # Fill in tiles of even indexed rows
   for i in range(0, size, size//4):
      for j in range(0, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0
         
   # Fill in tiles of odd indexed rows      
   for i in range(size//8, size, size//4):
      for j in range(size//8, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0

   plt.imsave("board.png", board)
   
   
   
# set up screen to 100(size)x100(size) and add background
def setupScreen(size):
   screen = turtle.Screen()
   screen.setup(size+100, size+100)
   screen.bgpic("board.png")


# create turtle with pieceColor, circle shape, and pen up
def createPiece(pieceColor):
   riva = turtle.Turtle()
   riva.color(pieceColor)
   riva.shape("circle")
   riva.penup()
   return riva


# move Piece to coordX, coordY
def movePiece(size, piece, row, col):
   # calculating x coordinate and y coordinate based on board size, row, and col provided
   coordX = size//-2 + size//16 + ((col - 1) * size//8)
   coordY = size//2 - size//16 - ((row - 1) * size//8)
   piece.goto(coordX, coordY)
 
# input checkerboard size, call drawBoard and setupScreen, call createPiece with red, ask row and col, call movePiece     
def main():
   size = int(input("Enter size of checkerboard: "))
   drawBoard(size)
   setupScreen(size)
   piece = createPiece("red")
   row = int(input("Enter row to move piece to: "))
   col = int(input("Enter col to move piece to: "))
   movePiece(size, piece, row, col)
   
   
if __name__ == "__main__":
   main()
