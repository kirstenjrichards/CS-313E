# File: TopoSort.py
# Description: This program takes in input and perfroms a topographical sort
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: November 17, 2022
# Date Last Modified: November 26, 2022

import sys
import itertools

# Add Your functions here
def maximum_profit(money, num_houses, prices, increase, possible_combinations):

    profit = 0
    for combination in possible_combinations:
        future_value = 0
        for price in combination:
            future_value += increase[prices.index(price)] * price

        if future_value > profit:
            profit = future_value

    return (profit / 100)

def all_combinations(list):

    combinations = []
    for l in range(len(list) + 1):
        for subset in itertools.combinations(list, l):
            combinations.append(subset)

    return combinations

# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer values} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   
    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])


# Add your implementation here .... 
    All_combinations = all_combinations(prices)
    possible_combinations = []
    for combination in All_combinations:
        if sum(combination) <= money:
            possible_combinations.append(combination)
    
    result =  maximum_profit(money, num_houses, prices, increase, possible_combinations)

# Add your functions and call them to generate the result. 

    print(result)

    
main()
