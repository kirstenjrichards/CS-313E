def print_adjacency_matrix(self):
        print("Adjacency matrix:")
        for row in self.adjMat:
          print ("".join(map(str,row)))

        # empty line afterwards
        print()

def bfs(self, start_index, color):
        
        self.reset_visited()
        
        print("Starting BFS; initial state:")
        
        Queue = Queue ()

        self.print_image()
        (self.nodes[start_index]).visited = True
        (self.nodes[start_index]).set_color(color)
        self.print_image()

        init_color = (self.nodes[start_index]).prev_color
        Queue.enqueue (start_index)

        while (not Queue.is_empty()):
          n1 = Queue.dequeue()

          n2 = self.get_adj_unvisited_node(n1, init_color)
          while (n2 != -1):
            (self.nodes[n2]).visited = True
            Queue.enqueue (n2)
            (self.nodes[n2]).set_color(color)
            self.print_image()
            n2 = self.get_adj_unvisited_node(n1, init_color)

        nVert = len (self.nodes)
        for i in range (nVert):
          (self.nodes[i]).visited = False

def dfs(self, start_index, color):
        
        self.reset_visited()
        
        print("Starting DFS; initial state:")

        Stack = Stack()
        ver_list = []

        self.print_image()
        (self.nodes[start_index]).visited = True
        (self.nodes[start_index]).set_color(color)
        self.print_image()

        init_color = (self.nodes[start_index]).prev_color
        ver_list.append(self.nodes[start_index])
        Stack.push (start_index)

        while (not Stack.is_empty()):
          
          u = self.get_adj_unvisited_node (Stack.peek(), init_color)
          if (u == -1):
            u = Stack.pop()
          else:
            (self.nodes[u]).visited = True
            ver_list.append(self.nodes[u])
            Stack.push(u)
            (self.nodes[u]).set_color(color)
            self.print_image()

        nVert = len (self.nodes)
        for i in range (nVert):
          (self.nodes[i]).visited = False