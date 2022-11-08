#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
	# Possible flowers number 1 to 9
	type_count = []
	flower_list.sort()
	counted = []
	for flower in flower_list:
		if flower not in counted:
			counted.append(flower)
			type_count.append(flower_list.count(flower))


	for vase in range(N):
		for flower in range(len(type_count)):
			type_count[flower] -= 2
			if type_count[flower] < 0:
				type_count[flower] = 0

	output_list = []
	for flower in range(len(type_count)):
		if type_count[flower] != 0:
			output_list.append(counted[flower])

	return output_list



if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
