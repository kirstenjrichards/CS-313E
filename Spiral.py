# File: Sprial.py
# Description:
# Student Name: Kirsten Richards
# Student UT EID:
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number:
# Date Created:
# Date Last Modified:

from re import X
import sys
import math
from tkinter import Spinbox
from collections import deque

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral( dimension ):
    
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

    print(spiral_list)
 
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the 
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers ( spiral, n ):
    pass

def main():
    # read the input file 
    # create the spiral
    # add the adjacent numbers 
    # print the result
    input_data = sys.stdin.read()
    data_list = list(input_data.split())
    create_spiral( int(data_list[0]))
    return_sum_list = []
    for data_num in range(1,len(data_list) - 1):
        return_sum_list.append(sum_adjacent_numbers(data_list[data_num]))

    print(return_sum_list)



if __name__ == "__main__":
    main()

