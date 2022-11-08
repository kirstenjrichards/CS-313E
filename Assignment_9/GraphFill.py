# File: TestBinaryTree.py
# Description: This program takes in a binary tree and tests it for the range of values in the tree, the level in which nodes are at,
# the left side view of the tree, and the sum of all leaf node values
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: November 4, 2022
# Date Last Modified: November 7, 2022

import os
import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color)*2, end='')

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------



# Stack class; you can use this for your search algorithms
class Stack(object):
  def __init__(self):
    self.stack = []

  # add an item to the top of the stack
  def push(self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek(self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty(self):
    return len(self.stack) == 0

  # return the number of elements in the stack
  def size(self):
    return len(self.stack)

# Queue class; you can use this for your search algorithms
class Queue(object):
  def __init__(self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue(self, item):
    self.queue.append(item)

  # remove an item from the beginning of the queue
  def dequeue(self):
    return self.queue.pop(0)

  # checks the item at the top of the Queue
  def peek(self):
    return self.queue[0]

  # check if the queue is empty
  def is_empty(self):
    return len(self.queue) == 0

  # return the size of the queue
  def size(self):
    return len(self.queue)

# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for serach algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def visit_and_set_color(self, color):
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))

# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size
        self.matrix = None

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):
        print("Adjacency matrix:")

        index = []
        for node in range(len(self.nodes)):
          x = self.nodes[node].x 
          y = self.nodes[node].y 
          row = self.nodes[node].edges

          index.append(row)

        matrix = []
        for row in range(len(index)):
          position = 0
          row_list = []
          for x in range(len(index)):
            if position in index[row]:
              row_list.append(1)
              position += 1
            else:
              row_list.append(0)
              position += 1
          matrix.append(row_list)
          self.matrix = matrix
        
        for x in range(len(matrix)):
          for y in range(len(matrix[x])):
            print(matrix[x][y], end = '')
          print()
        # empty line afterwards
        print()

    def get_adj_unvisited_node(self, v, color):
      nVert = len (self.nodes)
      for i in range (nVert):
        if (self.matrix[v][i] > 0) and (not (self.nodes[i]).visited) and (self.nodes[i]).color == color:
          return i
      return -1

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")

        self.print_image()

        queue = Queue()

        node1 = self.nodes[start_index]
        old_color = node1.color
        node1.visit_and_set_color(color)
        queue.enqueue(node1)
        self.print_image()

        while not queue.is_empty():
          node = queue.dequeue()
          for x in node.edges:
            edge_node = self.nodes[x]
            if edge_node.visited == False and edge_node.color == old_color:
              queue.enqueue(edge_node)
              edge_node.visit_and_set_color(color)
              self.print_image()
          

    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")

        node1 = self.nodes[start_index]
        old_color = node1.color

        node1.visit_and_set_color(color)
        self.print_image()
        for x in node1.edges:
          node = self.nodes[x]
          if node.color == old_color and not node.visited:
            self.dfs(x, color)



def create_graph(data):
    # creates graph from read in data
    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for i in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for i in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color


def main():
    # read input
    data = sys.stdin.read()

    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
