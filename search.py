import math

from utilities import utilities


class search:

    def __init__(self):
        self.nodes_count = 1
        self.tree_nodes = []
        self.tree_edges = []
        self.utility = utilities()
        self.depth = 0
    
    def search(self,node, player, K,depth = 0, alpha = -math.inf, beta = math.inf ):
        self.nodes_count = 1
        self.tree_nodes = []
        self.tree_edges = []
        self.depth = 0
        return self.__search(node, player, K,depth, alpha, beta )

    def __search(self,node, player, K,depth , alpha, beta ):
        if player == "AI":
            return self.search_AI(node, K, alpha , beta, depth)
        else:
            return self.search_human(node, K, alpha, beta,depth)  

    
    def search_human(self,node,K, alpha, beta, depth):
        human_cost = math.inf
        play = node
        nodes =self.utility.action(node, "h")
        depth += 1
        if(alpha == None):
            self.add_to_arrays(nodes)
        else:
            self.add_to_arrays(nodes, True)
        if(depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i)
       
                if(human_cost > hrstc):
                    play = i
                    play.node_score = hrstc
                    human_cost = hrstc
                    self.tree_nodes[i.node_num-1] = tuple([self.tree_nodes[i.node_num-1][0], human_cost])
                if(beta != None):
                    if(human_cost <= alpha):
                        play.node_score = human_cost
                        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],human_cost])
                        return play
                    beta = min(beta, human_cost)

        else:
            for i in nodes:
                val = self.__search(i, "AI", K, depth,alpha, beta)
                if(human_cost > val.node_score):
                    play = i
                    play.node_score = val.node_score
                    human_cost = val.node_score
                if(beta != None):
                  
                    if(human_cost <= alpha):
                        play.node_score = human_cost
                        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],human_cost]) 
                        return play
                    beta = min(beta, human_cost)
        play.node_score = human_cost
        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],human_cost])
        return play


    def search_AI(self,node,K, alpha, beta,depth):
        AI_cost = -math.inf
        play = node
        nodes =self.utility.action(node,"AI")
      
        if(alpha == None):
            self.add_to_arrays(nodes)
        else:
            self.add_to_arrays(nodes, True)
        depth += 1
        if(depth == 1):
            self.tree_nodes.insert(0,(str(node.node_num), 0))
        if(depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i)
                if(AI_cost < hrstc):
                    play = i
                    play.node_score = hrstc
                    AI_cost = hrstc
                self.tree_nodes[i.node_num-1] = tuple([self.tree_nodes[i.node_num-1][0], AI_cost])
                if(alpha != None):
                   
                    if(AI_cost >= beta):
                        play.node_score = AI_cost
                        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],AI_cost]) 
                        return play
                    alpha = max(alpha, AI_cost)
        else:
            for i in nodes:
                
                val = self.__search(i, "h",K, depth,alpha, beta)
                if(AI_cost < val.node_score):
                    play = i
                    play.node_score = val.node_score
                    AI_cost = val.node_score
                if(alpha != None):
                     
                    if(AI_cost >= beta):
                        play.node_score = AI_cost
                        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],AI_cost])
                        return play
                    alpha = max(alpha, AI_cost)
        play.node_score = AI_cost
        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],AI_cost]) 
        return play


    def add_to_arrays(self, nodes, pruning= False):
        
        for i in nodes:
            self.nodes_count += 1
            i.node_num = self.nodes_count
            if(pruning):
                self.tree_nodes.append((str(i.node_num), "pruned"))
            else:
                self.tree_nodes.append((str(i.node_num), 0))
            self.tree_edges.append((str(i.parent.node_num), str(i.node_num)))


    def print_nodes_edges(self):
        print(self.tree_nodes)
        print()
        print(self.tree_edges)
        print()



