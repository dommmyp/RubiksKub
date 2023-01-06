from piececube import *

class copy_cube:
   def __init__(self, cube):
      self.cube = Cube()
      self.cube.edges = [Edge(i) for i in range(12)]
      for i in range(12):
         self.cube.edges[i].align = cube.edges[i].align
         self.cube.edges[i].num = cube.edges[i].num

def solve(cube):
   solve_cross(cube)


def solve_cross(cube):
   moves = []
   piece_indices = [cube.get_index(i) for i in range(4)]
   aligned = [cube.edges[piece_indices[i]].align == 0 for i in range(4)]
   print(aligned)
   for i in range(4):
      done = False
      print("I " + str(i))
      for a in range(4):
         print("A " + str(a))
         for b in range(4):
            print("b " + str(b))
            result = align(moves, cube, piece_indices, 0, aligned, i)
            if result == []:
               done = True
               break
            if not result:
               cube.turn(0)
            else:
               done = True
               break
         if done:
            for x in result:
               print(x)
               cube.turn(x)
            break
         else:
            cube.turn(5)
                  
                     
         

   
def align(moves, cube, piece_indices, alignment, aligned, k):
   print("k " + str(piece_indices[k]))
   temp_cube = copy_cube(cube)
   temp_moves = moves.copy()
   piece_num = cube.edges[piece_indices[k]].num
   print("l " + str(cube.edges[piece_indices[k]].align))
   rerun = False
   if cube.edges[piece_indices[k]].align == alignment:
      print("yes")
      return temp_moves
   if cube.edges[piece_indices[k]].align == 1 and alignment == 0:
      match piece_indices[k]:
         case 4 | 5:
            temp_cube.cube.turn(1)
            temp_moves.append(1)
            print("y")
         case 6 | 7:
            temp_cube.cube.turn(3)
            temp_moves.append(3)
            print("y")
         case 0 | 1 | 2 | 3:
            temp_cube.cube.turn((6 - piece_indices[k]) % 4 + 1)
            temp_moves.append((6 - piece_indices[k]) % 4 + 1)
            rerun = True
            
         case 8 | 9 | 10 | 11:
            temp_cube.cube.turn((piece_indices[k] + 2) % 4 + 1)
            temp_moves.append((piece_indices[k] + 2) % 4 + 1)
            rerun = True

      if rerun:
         piece_indices = [temp_cube.cube.get_index(i) for i in range(4)]
         temp_moves = align(temp_moves, cube, piece_indices, alignment, aligned, k)
      # Check if alignment altered alignment of other pieces
      for i in range(len(aligned)):
         if cube.edges[i].align == 0 and temp_cube.cube.edges[i].align != 0 :
            print("fail")
            return False
      return temp_moves


   if cube.edges[piece_indices[k]].align == 2 and alignment == 0:
      match piece_indices[k]:
         case 5 | 6:
            temp_cube.cube.turn(4)
            temp_moves.append(4)
            print("y")
            return temp_moves
         case 4 | 7:
            temp_cube.cube.turn(2)
            temp_moves.append(2)
            print("y")
            return temp_moves
         case 0 | 1 | 2 | 3:
            temp_cube.cube.turn((6 - piece_indices[k]) % 4 + 1)
            temp_moves.append((6 - piece_indices[k]) % 4 + 1)
            rerun=True
         case 8 | 9 | 10 | 11:
            temp_cube.cube.turn((piece_indices[k] + 2) % 4 + 1)
            temp_moves.append((piece_indices[k] + 2) % 4 + 1)
            rerun = True

      if rerun:
         piece_indices = [temp_cube.cube.get_index(i) for i in range(4)]
         temp_moves = align(temp_moves, cube, piece_indices, alignment, aligned, k)
      # Check if alignment altered alignment of other pieces
      for i in range(len(aligned)):
         if not i == k:
            if cube.edges[i].align != temp_cube.cube.edges[i].align:
               return False
      return temp_moves


   # if cube.edges[piece_index].align == 0 and alignment == 1:
   #    pass
   # if cube.edges[piece_index].align == 2 and alignment == 1:
   #    pass
   # if cube.edges[piece_index].align == 0 and alignment == 2:
   #    pass
   # if cube.edges[piece_index].align == 1 and alignment == 2:
   #    pass


if __name__ == "__main__":
   cube = Cube()
   cube.scramble()
   cube.print()
   solve(cube)
   cube.print()

