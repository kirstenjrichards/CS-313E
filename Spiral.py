# File: Sprial.py
# Description:
# Student Name:
# Student UT EID:
# Partner Name:
# Partner UT EID:
# Course Name: CS 313E
# Unique Number:
# Date Created:
# Date Last Modified:

import sys
import math
from tkinter import Spinbox

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral( dimension ):
    
    spiral_list = []
    for row in range(dimension):
        spiral_row = []
        for col in range(dimension):
            spiral_row.append(0)
        spiral_list.append(spiral_row)
            

    x_location = math.ceil( dimension / 2 )
    y_location = math.ceil( dimension / 2 )

    for count in range(1, dimension ** 2):
        
        if count == 1:
            spiral_list[x_location][y_location] = count
        else:
            pass

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

if __name__ == "__main__":
    main()

