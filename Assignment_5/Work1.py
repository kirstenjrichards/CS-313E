import time
import sys


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):

  sum = v
  runs = k
  while sum // runs != 0:
    v += sum // runs
    runs = runs * k

  return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  v = 1
  while sum_series(v, k) < n:
    v += 1
  return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):

  start = 1 #low
  end = n #high
  mid = 0

  while start <= end:

    mid = (start + end) // 2

    if sum_series(mid,k) >= n and sum_series(mid-1,k) < n and sum_series(mid+1,k) > n:
      return mid
  
    elif sum_series(mid,k)>n:
      end=mid-1   
  
    elif sum_series(mid,k)<n:
      start=mid+1 

    else:
      return mid

  return mid




def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
