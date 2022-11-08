#  File: marbles.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

'''
A row of magic marbles can magically move to the right or left based on their magic. 
We use an array of nonzero integers to represent the magic strength of each marble. 
A magic marble can move to the right if its magic strength is positive and left otherwise. 
The power of each marble is computed by squared its magic strength. 
Assuming that each marble moves at the same speed, some marble will meet. 
If two marbles meet, the one with less power disappears. 
If both marbles have the same power, both marbles disappear. 
Return the array after all such meetings have occurred. 
Two marbles moving in the same direction will not meet. 
'''

import sys

# Input:  marbles is a list of nonzero integers
# Output: return a list representing marbles after all meetings have occurred

    
def get_marble_list(marbles):
    removal = True
    while removal == True:
        removal = False
        i = 0
        while len(marbles) != 0 and i < len(marbles):
            marble1 = marbles[i]
            if marble1 < 0 and i > 0:
                j = i - 1
                marble2 = marbles[j]
                if marble2 > 0:
                    removal = True
                    if marble2 ** 2 > marble1 ** 2:
                        marbles.pop(i)
                        i -= 1
                    elif marble2 ** 2 == marble1 ** 2:
                        marbles.pop(i)
                        marbles.pop(j)
                        i -= 2
                    else:
                        marbles.pop(j)
                        i -= 1
            elif marble1 > 0 and i < len(marbles) - 1:
                j = i + 1
                marble2 = marbles[j]
                if marble2 < 0:
                    removal = True
                    if marble2 ** 2 > marble1 ** 2:
                        marbles.pop(i)
                        i -= 1
                    elif marble2 ** 2 == marble1 ** 2:
                        marbles.pop(i)
                        marbles.pop(i)
                        i -= 2
                    else:
                        marbles.pop(j)
                        i -= 1
            i += 1
    return marbles
                        
                
                
# ***There is no reason to change anything below this line***

def main():
	marbles = [int(r) for r in sys.stdin.readline().strip().split(" ")]
	result = get_marble_list(marbles)
	print(result)

if __name__ == "__main__":
	main()
