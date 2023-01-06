from array import *
from enum import IntEnum
import random

class Color(IntEnum):
   WHITE = 0
   RED = 1
   BLUE = 2
   ORANGE = 3
   GREEN = 4
   YELLOW = 5
class Cube:

   def __init__(self):
      self.corners = [ [0]*4 for i in range(6)]
      self.edges = [ [0]*4 for i in range(6)]
      
      for i in range(6):
         for j in range(4):
            self.corners[i][j]=i
      
      for i in range(6):
         for j in range(4):
            self.edges[i][j]=i
   
   def turn(self, side):
      temp_edge = self.edges[side][3]
      temp_corner = self.corners[side][3]
      for i in range(3):
         self.edges[side][3-i]=self.edges[side][2-i]
         self.corners[side][3-i]=self.corners[side][2-i]
      self.edges[side][0]=temp_edge
      self.corners[side][0]=temp_corner
      match side:
         case Color.WHITE:
            self.turn_white()
         case Color.YELLOW:
            self.turn_yellow()
         case Color.RED:
            self.turn_red()
         case Color.ORANGE:
            self.turn_orange()
         case Color.BLUE:
            self.turn_blue()
         case Color.GREEN:
            self.turn_green()
   
   def turn_white(self):
      # Edges
      temp_edge = self.edges[Color.RED][0]
      self.edges[Color.RED][0]=self.edges[Color.BLUE][0]
      self.edges[Color.BLUE][0]=self.edges[Color.ORANGE][0]
      self.edges[Color.ORANGE][0]=self.edges[Color.GREEN][0]
      self.edges[Color.GREEN][0]=temp_edge
      # Corners
      temp_corner = self.corners[Color.RED][0]
      self.corners[Color.RED][0]=self.corners[Color.BLUE][0]
      self.corners[Color.BLUE][0]=self.corners[Color.ORANGE][0]
      self.corners[Color.ORANGE][0]=self.corners[Color.GREEN][0]
      self.corners[Color.GREEN][0]=temp_corner

      temp_corner = self.corners[Color.RED][1]
      self.corners[Color.RED][1]=self.corners[Color.BLUE][1]
      self.corners[Color.BLUE][1]=self.corners[Color.ORANGE][1]
      self.corners[Color.ORANGE][1]=self.corners[Color.GREEN][1]
      self.corners[Color.GREEN][1]=temp_corner

   def turn_yellow(self):
      # Edges
      temp_edge = self.edges[Color.RED][2]
      self.edges[Color.RED][2]=self.edges[Color.GREEN][2]
      self.edges[Color.GREEN][2]=self.edges[Color.ORANGE][2]
      self.edges[Color.ORANGE][2]=self.edges[Color.BLUE][2]
      self.edges[Color.BLUE][2]=temp_edge
      # Corners
      temp_corner = self.corners[Color.RED][0]
      self.corners[Color.RED][2]=self.corners[Color.GREEN][2]
      self.corners[Color.GREEN][2]=self.corners[Color.ORANGE][2]
      self.corners[Color.ORANGE][2]=self.corners[Color.BLUE][2]
      self.corners[Color.BLUE][2]=temp_corner

      temp_corner = self.corners[Color.RED][3]
      self.corners[Color.RED][3]=self.corners[Color.GREEN][3]
      self.corners[Color.GREEN][3]=self.corners[Color.ORANGE][3]
      self.corners[Color.ORANGE][3]=self.corners[Color.BLUE][3]
      self.corners[Color.BLUE][3]=temp_corner
   
   def turn_red(self):
      # Edges
      temp_edge = self.edges[Color.WHITE][2]
      self.edges[Color.WHITE][2]=self.edges[Color.GREEN][1]
      self.edges[Color.GREEN][1]=self.edges[Color.YELLOW][0]
      self.edges[Color.YELLOW][0]=self.edges[Color.BLUE][3]
      self.edges[Color.BLUE][3]=temp_edge
      # Corners
      temp_corner = self.corners[Color.WHITE][2]
      self.corners[Color.WHITE][2]=self.corners[Color.GREEN][1]
      self.corners[Color.GREEN][1]=self.corners[Color.YELLOW][0]
      self.corners[Color.YELLOW][0]=self.corners[Color.BLUE][3]
      self.corners[Color.BLUE][3]=temp_corner

      temp_corner = self.corners[Color.WHITE][3]
      self.corners[Color.WHITE][3]=self.corners[Color.GREEN][2]
      self.corners[Color.GREEN][2]=self.corners[Color.YELLOW][1]
      self.corners[Color.YELLOW][1]=self.corners[Color.BLUE][0]
      self.corners[Color.BLUE][0]=temp_corner

   def turn_orange(self):
      # Edges
      temp_edge = self.edges[Color.WHITE][0]
      self.edges[Color.WHITE][0]=self.edges[Color.BLUE][1]
      self.edges[Color.BLUE][1]=self.edges[Color.YELLOW][2]
      self.edges[Color.YELLOW][2]=self.edges[Color.GREEN][3]
      self.edges[Color.GREEN][3]=temp_edge
      # Corners
      temp_corner = self.corners[Color.WHITE][0]
      self.corners[Color.WHITE][0]=self.corners[Color.BLUE][1]
      self.corners[Color.BLUE][1]=self.corners[Color.YELLOW][2]
      self.corners[Color.YELLOW][2]=self.corners[Color.GREEN][3]
      self.corners[Color.GREEN][3]=temp_corner

      temp_corner = self.corners[Color.WHITE][1]
      self.corners[Color.WHITE][1]=self.corners[Color.BLUE][2]
      self.corners[Color.BLUE][2]=self.corners[Color.YELLOW][3]
      self.corners[Color.YELLOW][3]=self.corners[Color.GREEN][0]
      self.corners[Color.GREEN][0]=temp_corner
   
   def turn_blue(self):
      # Edges
      temp_edge = self.edges[Color.WHITE][1]
      self.edges[Color.WHITE][1]=self.edges[Color.RED][1]
      self.edges[Color.RED][1]=self.edges[Color.YELLOW][1]
      self.edges[Color.YELLOW][1]=self.edges[Color.ORANGE][3]
      self.edges[Color.ORANGE][3]=temp_edge
      # Corners
      temp_corner = self.corners[Color.WHITE][1]
      self.corners[Color.WHITE][1]=self.corners[Color.RED][1]
      self.corners[Color.RED][1]=self.corners[Color.YELLOW][1]
      self.corners[Color.YELLOW][1]=self.corners[Color.ORANGE][3]
      self.corners[Color.ORANGE][3]=temp_corner

      temp_corner = self.corners[Color.WHITE][2]
      self.corners[Color.WHITE][2]=self.corners[Color.RED][2]
      self.corners[Color.RED][2]=self.corners[Color.YELLOW][2]
      self.corners[Color.YELLOW][2]=self.corners[Color.ORANGE][0]
      self.corners[Color.ORANGE][0]=temp_corner

   def turn_green(self):
      # Edges
      temp_edge = self.edges[Color.WHITE][3]
      self.edges[Color.WHITE][3]=self.edges[Color.ORANGE][1]
      self.edges[Color.ORANGE][1]=self.edges[Color.YELLOW][3]
      self.edges[Color.YELLOW][3]=self.edges[Color.RED][3]
      self.edges[Color.RED][3]=temp_edge
      # Corners
      temp_corner = self.corners[Color.WHITE][3]
      self.corners[Color.WHITE][3]=self.corners[Color.ORANGE][1]
      self.corners[Color.ORANGE][1]=self.corners[Color.YELLOW][3]
      self.corners[Color.YELLOW][3]=self.corners[Color.RED][3]
      self.corners[Color.RED][3]=temp_corner

      temp_corner = self.corners[Color.WHITE][0]
      self.corners[Color.WHITE][0]=self.corners[Color.ORANGE][2]
      self.corners[Color.ORANGE][2]=self.corners[Color.YELLOW][0]
      self.corners[Color.YELLOW][0]=self.corners[Color.RED][0]
      self.corners[Color.RED][0]=temp_corner

   def print_face(self, face):
      print("|"+str(self.corners[face][0])+ " " + str(self.edges[face][0])+ " " +str(self.corners[face][1]) + "|")
      print("|"+str(self.edges[face][3])+ " " + str(face) + " " +str(self.edges[face][1]) + "|")
      print("|"+str(self.corners[face][3])+ " " + str(self.edges[face][2])+ " " +str(self.corners[face][2]) + "|")


   def print_cube(self):
      print("WHITE")
      self.print_face(Color.WHITE)
      print("RED")
      self.print_face(Color.RED)
      print("BLUE")
      self.print_face(Color.BLUE)
      print("ORANGE")
      self.print_face(Color.ORANGE)
      print("GREEN")
      self.print_face(Color.GREEN)
      print("YELLOW")
      self.print_face(Color.YELLOW)

   def scramble(self):
      num = random.randint(20,40)
      moves = [0]*num
      for i in range(num):
         moves[i] = random.randint(0,5)
         self.turn(moves[i])
      print(moves)

   def solve(self):
      self.solve_cross()

   def solve_cross(self):
      for i in range(1,4):
         pass




newCube = Cube()
newCube.scramble()
newCube.print_cube()

