#  File: ExpressionTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


    def __str__(self):
        return str(self.stack)


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


    


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):

        current_node = Node()

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
                self.tree_stack.pop()

            else:
                current_node.data = current_tok
                self.tree_stack.pop()
        
    

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        operators = []
        operands = []

        for i in range(len(aNode)):
            if (aNode[i] == '('):
                operators.append(aNode[i])

            elif (aNode[i] == ')'):
                while (len(operators)!=0 and operators[-1] != '('):
                # operand 1
                    operand1 = operands[-1]
                    operands.pop()
 
                # operand 2
                    operand2 = operands[-1]
                    operands.pop()
 
                # operator
                    operand3 = operators[-1]
                    operators.pop()

                    total = operand1 + operand2 + operand3
                    operands.append()

                operators.pop()

            elif (not anOperator(aNode[i])):
                operands.append(aNode[i] + "")


            else:
                while (len(operators)!=0 and priority(aNode[i]) <= priority(operators[-1])):
                    operand1 = operands[-1]
                    operands.pop()
 
                    operand2 = operands[-1]
                    operands.pop()
 
                    operand3 = operators[-1]
                    operators.pop()
 
                    total = operand1 + operand2 + operand3
                    operands.append(total)
                operators.append(aNode[i])


        while (len(operators)!=0):
            operand1 = operands[-1]
            operands.pop()
 
            operand2 = operands[-1]
            operands.pop()
 
            operand3 = operators[-1]
            operators.pop()
 
            total = operand1 + operand2 + operand3
            operands.append(total)
 

        return operands[-1]

    


        pass


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):

    


        pass


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

    print(tree.tree_stack)
    
    # evaluate the expression and print the result
    # print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    # print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    # print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
