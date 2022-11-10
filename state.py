class state:
    def __init__(self, board,col,Aiscore,humanscore,parent= None,node_num = 1):
        self.node_num = node_num
        self.node_score = 0
        self.board=board
        self.col=col
        self.Aiscore=Aiscore
        self.humanscore=humanscore
        self.parent=parent

       