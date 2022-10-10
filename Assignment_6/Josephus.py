import sys

class Link(object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, data ):
    newLink = Link(data)
    current = self.first
    newLink.next = self.first

    if (self.first == None):
      newLink.next = newLink
    else:
      while(current.next != self.first):
        current = current.next
      current.next = newLink
    self.first = newLink

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
#want to know if link has data we're looking for 
    while(current.next != self.first):
        if current.data == data:
          return current
        else:
          current = current.next
    if current.data == data:
          return current
        
    return None

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):

    current = self.first.next
    previous = self.first

    if (current == None):
      return None

    while(current.next != self.first.next):
        if current.data == data:
          #delete current
          #move pointer in previous to the one after current 
          #return first case after moving 
          previous.next = current.next
          return current
          
        else:
          previous = current
    
          current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current



  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    # Return the soldier/link to eliminate
    kill_soldier = self.find(start).data 
    #^^ helps us find the start list, guesses data value from start
    #do manually, have for loop "for x in range", start = start.next n times 
    return self.find(kill_soldier).next, self.delete(kill_soldier)
    #soldier we want to kill is in from the start, 


  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__(self):
    return str(self.first)
    #iterate through everything in list and add data value to string in the same way in insert/delete etc, go through every value once


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
  soldiers = CircularList()
  for x in range(1, num_soldiers + 1):
    soldiers.insert(x)

  while num_soldiers > 1:
    start_count, dead = soldiers.delete_after(start_count, elim_num)
    print(dead)
    num_soldiers -= 1


if __name__ == "__main__":
  main()
