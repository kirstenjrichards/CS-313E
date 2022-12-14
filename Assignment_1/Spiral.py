# File: Sprial.py
# Description: This program is designed to take in an input file, use the first line to as dimensions for an Ulma spiral, then calculate the surrounding numbers of
# remaining line numbers
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: September 1, 2022
# Date Last Modified: September 7, 2022

from re import X
import sys
import math
from collections import deque

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral( dimension ):

    # validation code to make sure the dimension is odd if not adds 1 to make it odd
    if dimension % 2 == 0:
        dimension += 1 
    
    # The below block of code creates a 2d list filled with 0's with the given paremeter dimension
    spiral_list = []
    for row in range(dimension):
        spiral_row = []
        for col in range(dimension):
            spiral_row.append(0)
        spiral_list.append(spiral_row)
            
    # The below constants set up the center of the spiral as the starting point
    x_location = math.ceil( dimension // 2 )
    y_location = math.ceil( dimension // 2 )

    radius = 1 
    step = 0
    times = 0
    count = 1

    # The below block of code sets up a dictionary for the corresponding coordinate adjustments and what direction the spiral is unfurling 
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1,0), "left": (0, -1)}
    order = deque(["right", "down", "left", "up"])
    direction = directions["right"]

    # The below block of code is designed to iterate throughout the matrix updating each value
    for num in range(dimension ** 2):
        spiral_list[x_location][y_location] = count
        count += 1 
        x_location += direction[0]
        y_location += direction[1]
        step += 1 
        if step == radius:
            step = 0
            order.rotate(-1)
            direction = directions[order[0]]
            times += 1
            if times == 2:
                times = 0
                radius += 1 

    return spiral_list
 
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the 
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers ( spiral, n):

     if int(n) > (dimension ** 2) or int(n) < 1:
         return 0

     sum = 0 
     # print(spiral)
     x = 0 
     y = 0
     for i in range(int(data_list[0])):
        for j in range(int(data_list[0])):
            # print(n,i,j,spiral[i][j])
            if int(n) == int(spiral[i][j]):
                # print("hi")
                x = i 
                y = j 
     
     # print(x,y)
     # print(sum)
     # up

     # the below block of code is designed to count up all the adjacent cells sorrounding the target cell
     if x != 0:
         sum += spiral[x-1][y]
     # up/right
     if x != 0 and y != int(data_list[0]) - 1:
         sum += spiral[x-1][y+1]
     # right
     if y != int(data_list[0]) - 1:
         sum += spiral[x][y+1]
     # right/down
     if x != int(data_list[0]) - 1 and y != int(data_list[0]) - 1:
         sum += spiral[x+1][y+1]
     # down
     if x != int(data_list[0]) - 1:
         sum += spiral[x+1][y]
     # down/left
     if x != int(data_list[0]) - 1 and y != 0:
         sum += spiral[x+1][y-1]
     # left
     if y != 0:
         sum += spiral[x][y-1]
     # up/left
     if x != 0 and y != 0:
         sum += spiral[x-1][y-1]
    
    
     return sum 
     
def main():
    # read the input file 
    # create the spiral
    # add the adjacent numbers 
    # print the result

    # the below block of code is designed to take the input file and split each line into a list for data extraction
    input_data = sys.stdin.read()
    global data_list
    data_list = list(input_data.split())

    # the below block of code is designed to create the spiral and set the dimension of the spiral for use within the file
    global dimension 
    dimension = int(data_list[0])
    data_spiral = create_spiral( int(data_list[0]))
    # print(data_spiral)

    # the below block of code is designed to call the adjancent numbers function by iterating over the input file line by line
    return_sum_list = []
    for data_num in range(len(data_list)):
        if data_num == 0:
            pass
        else:
            # print(data_list[data_num])
            return_sum_list.append(sum_adjacent_numbers(data_spiral, data_list[data_num]))

    # dimension = 15
    # test_spiral = create_spiral(15)
    # print(test_spiral)
    # return_sum_list.append(sum_adjacent_numbers(test_spiral, 193))
    
    # the below for statement is designed to convert the return list into a print line statement for each value
    for return_num in range(len(return_sum_list)):
        print(return_sum_list[return_num])


if __name__ == "__main__":
    main()

