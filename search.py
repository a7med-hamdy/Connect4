import math

from utilities import utilities


class search:

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.utility = utilities()
        self.explored = set()
        

    def search(self,node, player, K,alpha = -math.inf, beta = math.inf ):
        if player == "AI":
            return self.search_AI(node, K, alpha , beta)
        else:
            return self.search_human(node, K, alpha, beta)  
    
    def search_human(self,node,K, alpha, beta):
        human_cost = -math.inf
        play = node
        nodes =self.utility.action(node, "h")
        depth = nodes[0].depth
       # print(len(nodes))
        #for i in nodes:
         #   print(f"from humans states{i.board:b}")
        if(depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i)
                if(human_cost > hrstc):
                    play = i
                    human_cost = hrstc
                if(beta != None):
                    #print("hi beta")
                    if(human_cost <= alpha):
                        return play
                    beta = min(beta, human_cost)

        else:
            for i in nodes:
                val = self.search(i, "AI", K, alpha, beta)
                if(human_cost > val.Aiscore-val.humanscore):
                    play = i
                    human_cost = val.Aiscore-val.humanscore
                if(beta != None):
                    #print("hi beta")
                    if(human_cost <= alpha):
                        return play
                    beta = min(beta, human_cost)
        return play


    def search_AI(self,node,K, alpha, beta):
        AI_cost = -math.inf
        play = node
        nodes =self.utility.action(node,"AI")
        #for i in nodes:
            #print(f"from Bot states{i.board:b}")
        depth = nodes[0].depth
        if(depth == K):
            for i in nodes:
                hrstc =  self.utility.heuristic(i)
                if(AI_cost < hrstc):
                    play = i
                    AI_cost = hrstc
                if(alpha != None):
                    #print("hi alpha")
                    if(AI_cost >= beta):
                        return play
                alpha = max(alpha, AI_cost)
        else:
            for i in nodes:
                val = self.search(i, "h",K, alpha, beta)
                if(AI_cost < val.Aiscore-val.humanscore):
                    play = i
                    AI_cost = val.Aiscore-val.humanscore
                if(alpha != None):
                        #print("hi alpha")
                    if(AI_cost >= beta):
                        return play
                    alpha = max(alpha, AI_cost)
        return play


    

