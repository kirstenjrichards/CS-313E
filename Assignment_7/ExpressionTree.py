# File: ExpressionTree.py
# Description: This program takes in an expression creates an expression tree, evaluates the tree, and creates post/pre fix expressions
# Student Name: Kirsten Richards
# Student UT EID: KJR2599
# Partner Name: Steven Campbell
# Partner UT EID: SWC776
# Course Name: CS 313E
# Unique Number: 52520
# Date Created: October 16, 2022
# Date Last Modified: October 19, 2022

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


    def __str__(self):
        for x in self.stack:
            print(x.data)


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
        self.tree_stack = Stack()

    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):

        self.root = Node()

        current_node = self.root

        expr = expr.split(' ')
        for x in range(len(expr)):
            current_tok = expr[x]

            if current_tok == '(':
                current_node.lChild = Node()
                self.tree_stack.push(current_node)
                current_node = current_node.lChild
            
            elif current_tok in operators:
                current_node.data = current_tok
                self.tree_stack.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild
            
            elif current_tok == ')':
                if (node := self.tree_stack.pop()) is not None:
                    current_node = node
            else:
                if float(current_tok) % 1 == 0:
                    current_node.data = int(current_tok)
                else:
                    current_node.data = float(current_tok)
                current_node = self.tree_stack.pop()
            


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.lChild == None and aNode.rChild == None:
            return aNode.data
        elif aNode.data == '**':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child ** right_child)
        elif aNode.data == '%':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child % right_child)
        elif aNode.data == '//':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child // right_child)
        elif aNode.data == '+':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child + right_child)
        elif aNode.data == '-':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child - right_child)
        elif aNode.data == '*':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child * right_child)
        elif aNode.data == '/':
            left_child = self.evaluate(aNode.lChild)
            right_child = self.evaluate(aNode.rChild)
            return float(left_child / right_child)

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):

        if aNode != None:
            expression = str(aNode.data)
            if aNode.lChild != None:
                expression += ' ' + str(self.pre_order(aNode.lChild))
            if aNode.rChild != None:
                expression += ' ' + str(self.pre_order(aNode.rChild))

        return expression


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):

        if Node == type(aNode):
            expression = str(aNode.data)
            if aNode.rChild != None:
                expression = str(self.post_order(aNode.rChild) + ' ' + expression)
            if aNode.lChild != None:
                expression = str(self.post_order(aNode.lChild) + ' ' + expression)

        return expression


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
