import math
from random import randint

from utilities import utilities


class search:
    """
        minmax searching class 
    """

    def __init__(self):

        """
            constructor: initializes the search class with all its variables
        """
        #nodes counter used for indexing and building the decision tree
        self.nodes_count = 1
        # array to hold the tree nodes 
        self.tree_nodes = []
        self.tree_nodes_max = []
        self.tree_nodes_min = []
        # array to hold the tree edges
        self.tree_edges = []
        #utility class used to decide and get new actions 
        self.utility = utilities()


    def search(self,node, player, K,depth = 0, alpha = -math.inf, beta = math.inf ):
    
        """
            wrapper search function using minmax algorithm with/without pruning
            works with pruning by default to work without 
            pruning set alpha and beta to None
            
            parameters:
            node: initial state node
            player: the current player string "AI" or "h"
            K: maximum depth for search
            depth: current depth of the tree set by default to 0(at the start)
            alpha: set to -∞ by default 
            beta: set to ∞ by default 

            returns: the state played by the AI
        """
        #reset the global variables for each new search to draw a new tree
        self.nodes_count = 1
        self.tree_nodes = []
        self.tree_edges = []
        #call the recursive searching function
        return self.__search(node, player, K,depth, alpha, beta )

    def __search(self,node, player, K,depth , alpha, beta ):
        
        """
            search function using minmax algorithm with/without pruning
            works with pruning by default to work without 
            pruning set alpha and beta to None
            
            parameters:
            node: initial state node
            player: the current player string "AI" or "h"
            K: maximum depth for search
            depth: current depth of the tree set by default to 0(at the start)
            alpha: set to -∞ by default 
            beta: set to ∞ by default 

            returns: the state played by the AI
        """
        #if the current player is the AI(maximizing player)
        if player == "AI":
            #call the AI search function
            return self.search_AI(node, K, alpha , beta, depth)
        else:# if the current player is the human(minimizing player)
            #call the human search function
            return self.search_human(node, K, alpha, beta,depth)  

    
    def search_human(self,node,K, alpha, beta, depth):
        
        """
            search function as the human(minimizing player) 
            using minmax algorithm with/without pruning
                        
            parameters:
            node: initial state node
            K: maximum depth for search
            depth: current depth of the tree set by default to 0(at the start)
            alpha: set to -∞ by default 
            beta: set to ∞ by default 

            returns: the state played by the human
        """
        human_cost = math.inf   #initial cost max number
        play = node     #initial starting state
        nodes =self.utility.action(node, "h")   #do all possible actions as a human
        depth += 1  #increase the depth
        tieset = set() #set to determine if the a tie happened at a given node
        #this section is for building the tree
        if(alpha == None):
            self.add_to_arrays(nodes,player= "AI")
        else:
            self.add_to_arrays(nodes, player= "AI",pruning = True)
        
        #if we reached the maximum allowed depth we start using the heuristic function
        if(depth == K):
            #loop on all possible actions
            for i in nodes:
                hrstc =  self.utility.heuristic(i)  #calculate their heurisitc
                tieset.add(hrstc)   #add it to the tiebreaker set
                i.node_score = hrstc
                #choose the min between the current cost and the heuristc
                if(human_cost > hrstc):
                    play = i
                    play.node_score = hrstc
                    human_cost = hrstc
                #add the cost of the last node to it in the tree
                self.tree_nodes[i.node_num-1] = tuple([self.tree_nodes[i.node_num-1][0], human_cost, self.tree_nodes[i.node_num-1][2]])
                #if pruning is enabled 
                if(beta != None):
                    beta = min(beta, human_cost)
                    if(human_cost <= alpha):
                        break
                    
        #we have not reached the specified depth
        else:
            #loop on all possible actions
            for i in nodes:
                #search deeper into the tree as the opposite player
                val = self.__search(i, "AI", K, depth,alpha, beta)
                #add the node's score to the tiebreaker set 
                tieset.add(val.node_score)
                #choose the min between the current cost and the returned score
                if(human_cost > val.node_score):
                    play = i
                    play.node_score = val.node_score
                    human_cost = val.node_score
                #if pruning is enabled
                if(beta != None):
                    beta = min(beta, human_cost)
                    if(human_cost <= alpha):
                        break
        
        #print(f"from human depth {depth}",tieset)                    

        #if there is no pruning and there is a tie between all states
        if(alpha == None and len(tieset) == 1):
            #choose a random state
            play = nodes[randint(0, len(nodes)-1)]
        #set the score of the state's value to the cost returned from the previous loop
        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],human_cost, self.tree_nodes[node.node_num-1][2]])
        
        #play.node_score = human_cost
        return play


    def search_AI(self,node,K, alpha, beta,depth):
                
        """
            search function as the AI(maximizing player) 
            using minmax algorithm with/without pruning
                        
            parameters:
            node: initial state node
            K: maximum depth for search
            depth: current depth of the tree set by default to 0(at the start)
            alpha: set to -∞ by default 
            beta: set to ∞ by default 

            returns: the state played by the AI
        """
        AI_cost = -math.inf    #initial cost min number
        play = node #initial starting state
        nodes =self.utility.action(node,"AI") #do all possible actions as an AI
        tieset = set() #set to determine if the a tie happened at a given node
        #this section is for building the tree
        if(alpha == None):
            self.add_to_arrays(nodes,player= "human")
        else:
            self.add_to_arrays(nodes, player= "human",pruning =True)

        depth += 1 #increase the depth
        #this section is for building the tree since the this method does not take into account the root node
        if(depth == 1):
            self.tree_nodes.insert(0,(str(node.node_num), 0, "max"))
            
        #if we reached the maximum allowed depth we start using the heuristic function
        if(depth == K):
            #loop on all possible actions
            for i in nodes:
                hrstc =  self.utility.heuristic(i) #calculate their heurisitc
                tieset.add(hrstc) #add it to the tiebreaker set
                #choose the max between the current cost and the heuristc
                i.node_score = hrstc
                if(AI_cost < hrstc):
                    play = i
                    AI_cost = hrstc
                #add the cost of the last node to it in the tree
                self.tree_nodes[i.node_num-1] = tuple([self.tree_nodes[i.node_num-1][0], AI_cost, self.tree_nodes[i.node_num-1][2]])
                #if pruning is enabled 
                if(alpha != None):
                    alpha = max(alpha, AI_cost)
                    if(AI_cost >= beta):
                        break
        #we have not reached the specified depth
        else:
            #loop on all possible actions
            for i in nodes:
                #search deeper into the tree as the opposite player
                val = self.__search(i, "h",K, depth,alpha, beta)
                #add the node's score to the tiebreaker set
                tieset.add(val.node_score)
                #choose the max between the current cost and the returned score
                if(AI_cost < val.node_score):
                    play = i
                    play.node_score = val.node_score
                    AI_cost = val.node_score
                #if pruning is enabled
                if(alpha != None):
                    alpha = max(alpha, AI_cost)
                    if(AI_cost >= beta):
                        break
        #if there is no pruning and there is a tie between all states
        #print(f"from AI depth {depth}",tieset)                      
        if(alpha == None and len(tieset) == 1):
            #choose a random state
            play = nodes[randint(0, len(nodes)-1)]

        #set the score of the state's value to the cost returned from the previous loop
        self.tree_nodes[node.node_num-1] = tuple([self.tree_nodes[node.node_num-1][0],AI_cost, self.tree_nodes[node.node_num-1][2]]) 

        return play


    def add_to_arrays(self, nodes, player,pruning= False):
        """
            function to add the actions explored to the tree's nodes and edges

            parameters:
            nodes: list of all possible actions
            prunning: if pruning is enabled
        """
        #loop on all possible actions
        for i in nodes:
            #add the count of the nodes
            self.nodes_count += 1
            #set the number of the node 
            i.node_num = self.nodes_count
            #if pruning is enabled the we print "pruned" in the tree
            if(pruning):
                if(player == "human"):
                    self.tree_nodes.append((str(i.node_num), "pruned","min"))
                else:
                    self.tree_nodes.append((str(i.node_num), "pruned", "max"))
            #if not we append the a default cost of 0
            else:
                if(player == "human"):
                    self.tree_nodes.append((str(i.node_num), 0, "min"))
                else:
                    self.tree_nodes.append((str(i.node_num), 0, "max"))
            #join the parent with its children in the edges array
            self.tree_edges.append((str(i.parent.node_num), str(i.node_num)))

    #function to print the arrays for debugging
    def print_nodes_edges(self):
        print(self.tree_nodes)
        print()
        print(self.tree_edges)
        print()



