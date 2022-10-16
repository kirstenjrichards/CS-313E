# File: Josephus.py
# Description: This program takes in three inputs relating to num_soldiers, elim, and starting soldier to
# return the order of soldiers killed
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: October 8, 2022
# Date Last Modified: October 10, 2022

import sys
from collections import deque

class Link(object):
  def __init__ (self, data, next = None, previous=None):
    self.data = data
    self.next = next
    self.previous = previous

  def __str__(self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    if self.first == None:
      newLink = Link(data)
      self.first = newLink
      newLink.next = self.first
      newLink.previous = self.first
    else:
      newLink = Link(data)
      tail = self.first
      while tail.next != self.first:
        tail = tail.next
      tail.next = newLink
      newLink.previous = tail
      self.first.previous = newLink
      newLink.next = self.first

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):

    current = self.first
    if current == None:
      return None

    while current.next.data != data and current.next != self.first:
      current = current.next
    current = current.next
    if current.data == data:
      return current
    else:
      return None

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):

    current = self.find(data)
    
    if current == None:
      return None
    elif current == self.first:
      current.next.previous = current.previous 
      current.previous.next = current.next
    elif current != self.first:
      current.next.previous = current.previous
      current.previous.next = current.next
    if current == current.next:
      self.first = None
    return current

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    # Return the soldier/link to eliminate
    current = self.find(start)
    for i in range(1, n):
      current = current.next
    next_link = current.next
    self.delete(current.data)
    return current, next_link


  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    output_list = []
    current = self.first
    if current != None:
      while current.next != self.first:
        output_list.append(current.data)
        current = current.next
      output_list.append(current.data)
    return str(output_list)


def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  list1 = CircularList()
  for i in range(1, num_soldiers + 1):
    list1.insert(i)
  start = start_count
  for j in range(num_soldiers):
    x = list1.delete_after(start, elim_num)
    start_link = x[1]
    start = start_link.data
    delete_link = x[0]
    print(delete_link.data)


if __name__ == "__main__":
  main()
