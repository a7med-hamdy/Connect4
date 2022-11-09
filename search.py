import math

from utilities import utilities


class search:

    def __init__(self):
        self.utility = utilities()
        self.explored = set()
        self.depth = 0

    def search(self,node, player, K, alpha = -math.inf, beta = -math.inf):

        if player == "AI":
            return self.search_AI(node, K, alpha , beta)
        else:
            return self.search_human(node, K, alpha, beta)  
    
    def search_human(self,node,K, alpha, beta):
        human_cost = -math.inf
        play = node
        nodes =self.utility.action(node, "h")
        self.depth = max(nodes[0].depth, self.depth)
        if(self.depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i.board)
                if(human_cost < hrstc):
                    play = i
                    human_cost = hrstc
                    if(beta != None):
                        beta = max(beta, human_cost)
                        if(human_cost > alpha):
                            return human_cost
        else:
            for i in nodes:
                val = self.search(i, "AI", K, alpha, beta)
                if(human_cost < val):
                    play = i
                    human_cost = val
                    if(beta != None):
                        beta = max(beta, human_cost)
                        if(human_cost > alpha):
                            return human_cost
        return human_cost


    def search_AI(self,node,K, alpha, beta):
        AI_cost = -math.inf
        play = node
        nodes =self.utility.action(node,"AI")
        self.depth = max(nodes[0].depth, self.depth)
        if(self.depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i.board)
                if(AI_cost < hrstc):
                    play = i
                    AI_cost = hrstc
                    if(alpha != None):
                        alpha = max(alpha, AI_cost)
                        if(AI_cost > beta):
                            return AI_cost
        else:
            for i in nodes:
                val = self.search(i, "h",K, alpha, beta)
                if(AI_cost < val):
                    play = i
                    AI_cost = val
                    if(alpha != None):
                        alpha = max(alpha, AI_cost)
                        if(AI_cost > beta):
                            return AI_cost
        return AI_cost


    

