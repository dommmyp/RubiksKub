from array import *
from enum import IntEnum
import random

class Corner:
   def __init__(self):
      self.align = 0
class Edge:
   def __init__(self, num):
      self.align = 0
      self.num = num

class Cube:
   def __init__(self):
      self.edges = [Edge(i) for i in range(12)]
      self.corners = [i for i in range(8)]
      for i in range(4,8):   
         self.edges[i].align = 1

   def turn(self, side):
      print("turn")
      self.turn_edges(side)
      # self.turn_corners(side)
   
   def turn_edges(self, side):
      match side:
         case 0:
            temp = self.edges[0]
            self.edges[0] = self.edges[3]
            self.edges[3] = self.edges[2]
            self.edges[2] = self.edges[1]
            self.edges[1] = temp
            if self.edges[1].align == 2:
               self.edges[1].align = 1
            if self.edges[2].align == 1:
               self.edges[2].align = 2
            if self.edges[3].align == 2:
               self.edges[3].align = 1
            if self.edges[0].align == 1:
               self.edges[0].align = 2
         case 1:
            temp = self.edges[2]
            self.edges[2] = self.edges[5]
            self.edges[5] = self.edges[10]
            self.edges[10] = self.edges[4]
            self.edges[4] = temp
            if self.edges[4].align == 0:
               self.edges[4].align = 1
            if self.edges[10].align == 1:
               self.edges[10].align = 0
            if self.edges[5].align == 0:
               self.edges[5].align = 1
            if self.edges[2].align == 1:
               self.edges[2].align = 0

         case 2:
            temp = self.edges[1]
            self.edges[1] = self.edges[4]
            self.edges[4] = self.edges[11]
            self.edges[11] = self.edges[7]
            self.edges[7] = temp
            if self.edges[7].align == 0:
               self.edges[7].align = 2
            if self.edges[11].align == 2:
               self.edges[11].align = 0
            if self.edges[4].align == 0:
               self.edges[4].align = 2
            if self.edges[1].align == 2:
               self.edges[1].align = 0
         case 3:
            temp = self.edges[0]
            self.edges[0] = self.edges[7]
            self.edges[7] = self.edges[8]
            self.edges[8] = self.edges[6]
            self.edges[6] = temp
            if self.edges[6].align == 0:
               self.edges[6].align = 1
            if self.edges[8].align == 1:
               self.edges[8].align = 0
            if self.edges[7].align == 0:
               self.edges[7].align = 1
            if self.edges[0].align == 1:
               self.edges[0].align = 0
         case 4:
            temp = self.edges[3]
            self.edges[3] = self.edges[6]
            self.edges[6] = self.edges[9]
            self.edges[9] = self.edges[5]
            self.edges[5] = temp
            if self.edges[5].align == 0:
               self.edges[5].align = 2
            if self.edges[9].align == 2:
               self.edges[9].align = 0
            if self.edges[6].align == 0:
               self.edges[6].align = 2
            if self.edges[3].align == 2:
               self.edges[3].align = 0
         case 5:
            temp = self.edges[8]
            self.edges[8] = self.edges[11]
            self.edges[11] = self.edges[10]
            self.edges[10] = self.edges[9]
            self.edges[9] = temp
            if self.edges[9].align == 2:
               self.edges[9].align = 1
            if self.edges[10].align == 1:
               self.edges[10].align = 2
            if self.edges[11].align == 2:
               self.edges[11].align = 1
            if self.edges[8].align == 1:
               self.edges[8].align = 2

   def scramble(self):
      num = random.randint(15,20)
      # moves = [0]*num
      moves = [4, 4, 1, 3, 3, 4, 4, 5, 3, 0, 4, 0, 4, 3, 1, 5]
      for i in range(len(moves)):
         # moves[i] = random.randint(0,5)
         self.turn(moves[i])
      print(moves)

   def get_index(self, n):
      index = -1
      for i in range(12):
         if self.edges[i].num == n:
            index = i
      return index

   def print(self):
      for i in range(12):
         print(str(i) + ":" + str(self.edges[i].num) + ", " + str(self.edges[i].align))
